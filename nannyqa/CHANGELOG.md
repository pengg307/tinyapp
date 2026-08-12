# 更新日志 - 家政面试题库系统

## v3.2 (2026-08-12)

### 重大改进：易记短码 + 直接链接查看报告

#### 1. 短码系统
- **旧方式**: UUID格式（如 `868abd4e-a5d`），难以记忆
- **新方式**: 6位字母数字组合（如 `HCVFFE`），易读易记
- 生成规则：排除易混淆字符 0/O/1/I/l，确保清晰可读

#### 2. 直接链接查看报告
- **新端点**: `GET /report/{short_code}`
- **功能**: 无需登录，直接访问报告页面
- **URL示例**: `http://localhost:8005/report/HCVFFE`
- 支持分享链接给雇主查看

#### 3. API变更
```python
# 创建会话 - 返回短码
POST /api/session
{
  "master_name": "Alice",
  "company": "ACorp"
}

# 响应
{
  "short_code": "HCVFFE",           # 易记短码
  "test_url": "http://.../test/HCVFFE",
  "report_url": "http://.../report/HCVFFE",
  "master_info": {"name": "Alice", "company": "ACorp"}
}
```

#### 4. 前端修复
- 变量名从 `currentSessionId` 改为 `currentSessionCode`
- 显示字段从 `data.session_id` 改为 `data.short_code`
- 占位符从 "例如: abc123def456" 改为 "例如: Y9XJKM"
- 雇主信息显示从 `data.master_name` 改为 `data.master_info?.name`

### 使用流程
1. 雇主打开 http://localhost:8005
2. 输入姓名、公司等信息
3. 点击"生成二维码"
4. 系统显示短码（如 `HCVFFE`）和两个URL
5. 发送测试链接 `http://.../test/HCVFFE` 给应聘者
6. 应聘者扫码答题
7. 完成后，雇主可直接访问 `http://.../report/HCVFFE` 查看报告
