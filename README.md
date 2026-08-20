# md2docx-cn

把 UTF-8 Markdown 中文文章转换成排版整洁的 Word 文档，适合投稿、方案、
公众号长文留档和日常办公交付。

## 能做什么

- 识别一至三级标题、普通段落、项目符号、编号步骤和引用。
- 自动应用中文字体、首行缩进、行距、页边距和标题层级。
- 写入文档标题与作者元数据。
- Windows、macOS 和 Linux 均可运行，输入文件保持在本机处理。

## 快速开始

需要 Python 3.10 或更高版本。

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
md2docx-cn examples/sample.md -o sample.docx --author "你的名字"
```

macOS 或 Linux 激活环境时使用 `source .venv/bin/activate`。

## 支持的 Markdown

```markdown
# 文档标题

普通正文段落。

## 小节

- 项目一
- 项目二

1. 第一步
2. 第二步

> 一段引用或提示。
```

## 商业服务

免费版适合通用中文文章。需要匹配单位模板、投稿格式或批量流程时，可在
[定制排版 Issue](../../issues/new?template=custom-template.yml) 中说明需求。

试运营参考价：

- 99 元：调整一套现有排版参数。
- 299 元：制作一套专用 Word 模板，含一次修改。
- 699 元起：批量转换、目录规则或现有工作流集成。
- 999 元起：团队内部工具、品牌化封装或 OEM 集成。
- 199 元/月起：模板维护、兼容性升级和优先技术支持。

完整服务边界、交付内容和合作流程见 [商业服务说明](COMMERCIAL.md)。基础代码仍按
MIT License 开放；收费部分是需求分析、私有模板、集成实施、维护和支持。

业务联系邮箱：[1066536086@qq.com](mailto:1066536086@qq.com)。提交公开 Issue 后，
请通过邮件发送 Issue 链接；报价、支付宝付款方式、私有材料和交付信息均不在公开
Issue 中传递。付款节点和验收规则见 [付款与交付说明](PAYMENT.md)。

提交需求不等于下单。先确认文件格式、交付边界、价格和时间，再决定是否合作；
Issue 是公开页面，请勿上传隐私材料、未发表全文、密钥或客户数据。

## 验证

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

## 当前边界

- 这是聚焦中文文章的 Markdown 子集转换器，不追求完整 CommonMark 兼容。
- 暂不解析图片、复杂表格、脚注、公式和嵌套列表。
- 不上传文档，不包含遥测，也不需要账号或 API 密钥。

## 开源许可

代码使用 [MIT License](LICENSE)。免费版可以自由使用和修改；付费服务出售的是
模板适配、批量自动化、部署和支持，而不是限制用户使用基础代码。
