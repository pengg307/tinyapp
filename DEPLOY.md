# 部署方式：Vercel Git Integration（推荐）

## 为什么不用 GitHub Actions？

| 方式 | 优点 | 缺点 |
|------|------|------|
| **Vercel Git Integration** | 简单，连接仓库即可 | 需手动触发首次 |
| GitHub Actions | 完全自动化 | 需配置 3 个 Secrets |

## 使用 Vercel Git Integration

### Step 1: 删除 GitHub Actions workflow

```bash
cd E:/aiprojects/tinyapp
git rm .github/workflows/deploy.yml
git commit -m "feat: remove GitHub Actions workflow"
git push origin main
```

### Step 2: 连接 GitHub 到 Vercel

1. 打开 https://vercel.com/dashboard
2. 点击 "Add New..." → "Project"
3. 选择 `pengg307/tinyapp` 仓库
4. 点击 "Deploy"

### Step 3: 配置自动部署

1. 在 Vercel Dashboard 选择项目
2. Settings → Git → Automatically Rebuild on Push
3. 确保 Main Branch 设为 `main`

### Step 4: 每次只需 push

```bash
git add -A
git commit -m "your message"
git push origin main
```

→ Vercel 自动构建部署！

## 为什么这个更好？

- ✅ 不需要配置 Secrets
- ✅ 不需要 workflow 文件
- ✅ Vercel 官方支持，更稳定
- ✅ 只需 push 代码即可自动部署
