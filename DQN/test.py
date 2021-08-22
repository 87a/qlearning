#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:test  文件名称
# DateTime:2021/8/20 15:45  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import gym

# 超参数
BATCH_SIZE = 32
LR = 0.01  # learning rate
EPSILON = 0.9  # greedy policy
GAMMA = 0.9  # reward discount
TARGET_REPLACE_ITER = 100  # target update frequency
MEMORY_CAPACITY = 2000  # replay buffer

env = gym.make('CartPole-v0')  # 创建环境
env = env.unwrapped  # 据说不做这个动作会有很多限制，unwrapped是打开限制的意思
N_ACTIONS = env.action_space.n  # 2 actions
N_STATES = env.observation_space.shape[0]  # 4 states
ENV_A_SHAPE = 0 if isinstance(env.action_space.sample(), int) else env.action_space.sample().shape


# 定义网络
class Net(nn.Module):
    def __init__(self, ):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(N_STATES, 10)  # 第一层
        self.fc1.weight.data.normal_(0, 0.1)  # in-place initialization of weights of fc1
        self.out = nn.Linear(10, N_ACTIONS)  # 第二层
        self.out.weight.data.normal_(0, 0.1)  # in-place initialization of weights of fc2

    def forward(self, x):
        # 前向传播
        x = self.fc1(x)
        x = F.relu(x)
        action_value = self.out(x)
        return action_value


# 定义DQN
class DQN(object):
    def __init__(self):
        self.eval_net, self.target_net = Net(), Net()  # 定义eval_net和target_net
        self.learn_step_counter = 0  # 学习步数计数
        self.memory_counter = 0  # 记忆库中的位置
        self.memory = np.zeros((MEMORY_CAPACITY, N_STATES * 2 + 2))  # 初始化记忆库
        self.optimizer = torch.optim.Adam(self.eval_net.parameters(), lr=LR)  # 定义优化器
        self.loss_func = nn.MSELoss()  # 定义损失函数

    def choose_action(self, x):
        x = torch.unsqueeze(torch.FloatTensor(x), 0)  # 给输入增加一维
        if np.random.uniform() < EPSILON:  # greedy
            action_value = self.eval_net.forward(x)
            # torch.max()会返回两个tensor, 一个包含最大值,一个包含索引, 我们要第二个
            action = torch.max(action_value, 1)[1].data.numpy()
            action = action[0] if ENV_A_SHAPE == 0 else action.reshape(ENV_A_SHAPE)  # return the argmax index
        else:  # 随机选取
            action = np.random.randint(0, N_ACTIONS)
            action = action if ENV_A_SHAPE == 0 else action.reshape(ENV_A_SHAPE)
        return action

    def store_transition(self, s, a, r, s_):
        # 保存到记忆库
        # 需要保存的内容拼接在一起
        transition = np.hstack((s, [a, r], s_))
        # 如果容量已满,则用新记忆替换旧记忆, 未满则按顺序放入
        index = self.memory_counter % MEMORY_CAPACITY
        self.memory[index, :] = transition
        self.memory_counter += 1

    def learn(self):
        # 检测target_net是否需要更新
        if self.learn_step_counter % TARGET_REPLACE_ITER == 0:
            # 如果需要更新,将eval_net的参数复制到target_net
            self.target_net.load_state_dict(self.eval_net.state_dict())

        self.learn_step_counter += 1
        # 用minibatch训练
        sample_index = np.random.choice(MEMORY_CAPACITY,
                                        BATCH_SIZE)  # 获得随机的索引
        b_memory = self.memory[sample_index, :]  # 提取对应索引的记忆
        b_s = torch.FloatTensor(b_memory[:, :N_STATES])  # batch的state
        b_a = torch.LongTensor(b_memory[:, N_STATES: N_STATES + 1].astype(int))  # batch的action
        b_r = torch.FloatTensor(b_memory[:, N_STATES + 1: N_STATES + 2])  # batch的reward
        b_s_ = torch.FloatTensor(b_memory[:, -N_STATES:])  # batch的state_

        # 计算q_eval和q_target
        q_eval = self.eval_net(b_s).gather(1, b_a)
        q_next = self.target_net(b_s_).detach()
        q_target = b_r + GAMMA * q_next.max(1)[0].view(BATCH_SIZE, 1)

        # 计算损失函数
        loss = self.loss_func(q_eval, q_target)

        # 反向传播
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()


dqn = DQN()  # 创建实例

print('\nCollecting experience...')

for i_episode in range(400):
    # 主循环
    s = env.reset()  # 重置环境
    ep_r = 0
    while True:
        env.render()  # 渲染环境

        a = dqn.choose_action(s)

        # 做出动作
        s_, r, done, info = env.step(a)

        # 调整reward
        x, x_dot, theta, theta_dot = s_
        r1 = (env.x_threshold - abs(x)) / env.x_threshold - 0.8
        r2 = (env.theta_threshold_radians - abs(theta)) / env.theta_threshold_radians - 0.5
        r = r1 + r2
        dqn.store_transition(s, a, r, s_)

        ep_r += r
        if dqn.memory_counter > MEMORY_CAPACITY:
            dqn.learn()
            if done:
                print('Ep: ', i_episode,
                      '| Ep_r: ', round(ep_r, 2))

        if done:
            break
        s = s_
