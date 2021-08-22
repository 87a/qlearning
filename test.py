#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author:Administrator  作者
# FileName:test  文件名称
# DateTime:2021/8/17 20:13  当前时间
# SoftWare: PyCharm  创建文件的IDE名称

# plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
# plt.rcParams['axes.unicode_minus'] = False
import numpy as np
import pandas as pd
import time

np.random.seed(2)
N_STATES = 6
ACTIONS = ['left', 'right']
EPSILON = 0.9
ALPHA = 0.1
LAMBDA = 0.9
MAX_EPISODES = 13  # 训练次数
FRESH_TIME = 0.3  # 走一步花的时间


def build_q_table(n_states, actions):
    # 建立Q表
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),  # 全零初始化
        columns=actions,
    )
    # print(table)
    return table


# build_q_table(N_STATES, ACTIONS)
def choose_action(state, q_table):
    # 选择动作
    state_actions = q_table.iloc[state, :]
    if (np.random.uniform() > EPSILON) or (state_actions.all() == 0):  # act non_greedy
        action_name = np.random.choice(ACTIONS)
    else:  # act greedy
        action_name = state_actions.idxmax()
    return action_name


def get_env_feedback(S, A):
    # 环境反馈
    if A == 'right':  # 右移
        if S == N_STATES - 2:  # 在终点前
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else:  # 左移
        R = 0
        if S == 0:  # 在最左侧
            S_ = S
        else:
            S_ = S - 1
    return S_, R


def update_env(S, episode, step_counter):
    # 环境更新
    env_list = ['-'] * (N_STATES - 1) + ['T']  # '------T'
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode + 1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r                     ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print('\r{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)


def rl():
    # 主循环
    q_table = build_q_table(N_STATES, ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminated = False
        update_env(S=S, episode=episode, step_counter=step_counter)
        while not is_terminated:
            A = choose_action(state=S, q_table=q_table)
            S_, R = get_env_feedback(S=S, A=A)
            q_predict = q_table.loc[S, A]
            if S_ != 'terminal':
                q_target = R + LAMBDA * q_table.iloc[S_, :].max()
            else:
                q_target = R
                is_terminated = True

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)
            S = S_

            update_env(S=S, episode=episode, step_counter=step_counter + 1)
            step_counter += 1
    return q_table


if __name__ == '__main__':
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)
