# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

URD 是一个中文短篇小说写作技能库，包含一系列写作方法论和技巧，旨在提升短篇小说创作质量。

## 目录结构

```
短篇小说写作/
└── skills/           # 写作技能模块
    ├── fiction-style-guide/      # 去AI味写作规范
    ├── conflict-first-hook/      # 冲突先行导语设计法
    ├── deep-task-flow/           # 深度任务执行框架
    ├── hook-logic-checker/       # 导语逻辑检查工具
    ├── hook-reverse-analysis/    # 导语逆向分析
    ├── premortem/                # 错误预演方法论
    └── skill-feedback-report/    # 技能反馈报告
```

## 核心技能说明

### fiction-style-guide（去AI味写作规范）
核心理念：AI味的本质是不信任读者。包含红线清单（情绪标签、作者旁白、装饰性动作、陈腐比喻等禁用项）和替代策略。

### conflict-first-hook（冲突先行导语设计法）
流程：极端冲突 → 生活化动机 → 设定修补。先保证吸引力，再倒推合理性。

### hook-logic-checker（导语逻辑检查）
检查标准：主角行为逻辑是否成立 + 有无让读者出戏的细节。区分"悬念"与"困惑"。

### deep-task-flow（深度任务执行框架）
五阶段闭环：需求澄清 → 错误预演 → 计划制定 → 执行 → 检查。

### premortem（错误预演）
在执行前想象失败场景，识别陷阱，制定规避策略。

## 使用方式

每个技能模块包含 SKILL.md 文件，定义了触发条件和执行流程。部分技能包含 references/ 子目录存放示例和模板。
