<a name="readme-top"></a>

<div align="center">
  <img src="./docs/static/img/logo.png" alt="Logo" width="200">
  <h1 align="center">DEVINJP: コード少なく、創造多く</h1>
</div>


<div align="center">
  <a href="https://github.com/All-Hands-AI/DEVINJP/graphs/contributors"><img src="https://img.shields.io/github/contributors/All-Hands-AI/DEVINJP?style=for-the-badge&color=blue" alt="Contributors"></a>
  <a href="https://github.com/All-Hands-AI/DEVINJP/stargazers"><img src="https://img.shields.io/github/stars/All-Hands-AI/DEVINJP?style=for-the-badge&color=blue" alt="Stargazers"></a>
  <a href="https://codecov.io/github/All-Hands-AI/DEVINJP?branch=main"><img alt="CodeCov" src="https://img.shields.io/codecov/c/github/All-Hands-AI/DEVINJP?style=for-the-badge&color=blue"></a>
  <a href="https://github.com/All-Hands-AI/DEVINJP/blob/main/LICENSE"><img src="https://img.shields.io/github/license/All-Hands-AI/DEVINJP?style=for-the-badge&color=blue" alt="MIT License"></a>
  <br/>
  <a href="https://join.slack.com/t/devinjp-ai/shared_invite/zt-2ngejmfw6-9gW4APWOC9XUp1n~SiQ6iw"><img src="https://img.shields.io/badge/Slack-Join%20Us-red?logo=slack&logoColor=white&style=for-the-badge" alt="Join our Slack community"></a>
  <a href="https://discord.gg/ESHStjSjD4"><img src="https://img.shields.io/badge/Discord-Join%20Us-purple?logo=discord&logoColor=white&style=for-the-badge" alt="Join our Discord community"></a>
  <a href="https://github.com/All-Hands-AI/DEVINJP/blob/main/CREDITS.md"><img src="https://img.shields.io/badge/Project-Credits-blue?style=for-the-badge&color=FFE165&logo=github&logoColor=white" alt="Credits"></a>
  <br/>
  <a href="https://docs.all-hands.dev/modules/usage/getting-started"><img src="https://img.shields.io/badge/Documentation-000?logo=googledocs&logoColor=FFE165&style=for-the-badge" alt="Check out the documentation"></a>
  <a href="https://arxiv.org/abs/2407.16741"><img src="https://img.shields.io/badge/Paper%20on%20Arxiv-000?logoColor=FFE165&logo=arxiv&style=for-the-badge" alt="Paper on Arxiv"></a>
  <a href="https://huggingface.co/spaces/DEVINJP/evaluation"><img src="https://img.shields.io/badge/Benchmark%20score-000?logoColor=FFE165&logo=huggingface&style=for-the-badge" alt="Evaluation Benchmark Score"></a>
  <hr>
</div>

DEVINJP（旧OpenHands）へようこそ。AIを活用したソフトウェア開発エージェントのプラットフォームです。

DEVINJPエージェントは人間の開発者と同じことができます：コードの修正、コマンドの実行、ウェブの閲覧、
APIの呼び出し、そしてもちろん—StackOverflowからコードスニペットをコピーすることも。

詳細は[docs.all-hands.dev](https://docs.all-hands.dev)をご覧いただくか、[クイックスタート](#-quick-start)にジャンプしてください。

> [!IMPORTANT]
> 仕事でDEVINJPを使用していますか？ぜひお話を聞かせてください！
> [この短いフォーム](https://docs.google.com/forms/d/e/1FAIpQLSet3VbGaz8z32gW9Wm-Grl4jpt5WgMXPgJ4EDPVmCETCBpJtQ/viewform)
> に記入して、デザインパートナープログラムにご参加ください。商用機能への早期アクセスや製品ロードマップへの意見提供の機会が得られます。

![App screenshot](./docs/static/img/screenshot.png)

## ⚡ クイックスタート

DEVINJPを実行する最も簡単な方法はDockerを使用することです。
システム要件や詳細情報については[DEVINJPの実行](https://docs.all-hands.dev/modules/usage/installation)ガイドを
ご覧ください。

```bash
docker pull docker.all-hands.dev/all-hands-ai/runtime:0.31-nikolaik

docker run -it --rm --pull=always \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.31-nikolaik \
    -e LOG_ALL_EVENTS=true \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.devinjp-state:/.devinjp-state \
    -p 3000:3000 \
    --add-host host.docker.internal:host-gateway \
    --name devinjp-app \
    docker.all-hands.dev/all-hands-ai/devinjp:0.31
```

> [!WARNING]
> パブリックネットワーク上で使用する場合は、[強化されたDockerインストール](https://docs.all-hands.dev/modules/usage/runtimes/docker#hardened-docker-installation)ガイドを参照して、
> ネットワークバインディングを制限し、追加のセキュリティ対策を実装することでデプロイメントを保護してください。

DEVINJPは[http://localhost:3000](http://localhost:3000)で実行されています！

最後に、モデルプロバイダーとAPIキーが必要です。
[AnthropicのClaude 3.5 Sonnet](https://www.anthropic.com/api) (`anthropic/claude-3-5-sonnet-20241022`)
が最も効果的ですが、[他にも多くの選択肢](https://docs.all-hands.dev/modules/usage/llms)があります。

---

また、[DEVINJPをローカルファイルシステムに接続](https://docs.all-hands.dev/modules/usage/runtimes/docker#connecting-to-your-filesystem)したり、
[ヘッドレスモード](https://docs.all-hands.dev/modules/usage/how-to/headless-mode)でスクリプト化して実行したり、
[使いやすいCLI](https://docs.all-hands.dev/modules/usage/how-to/cli-mode)で操作したり、
[GitHubアクション](https://docs.all-hands.dev/modules/usage/how-to/github-action)でタグ付けされた課題に対して実行することもできます。

詳細なセットアップ手順については[DEVINJPの実行](https://docs.all-hands.dev/modules/usage/installation)をご覧ください。

> [!CAUTION]
> DEVINJPはローカルワークステーションで単一ユーザーによって実行されることを想定しています。
> 複数のユーザーが同じインスタンスを共有するマルチテナント環境には適していません。組み込みの分離機能やスケーラビリティはありません。
>
> マルチテナント環境でDEVINJPを実行することに興味がある場合は、
> 高度なデプロイメントオプションについて[お問い合わせください](https://docs.google.com/forms/d/e/1FAIpQLSet3VbGaz8z32gW9Wm-Grl4jpt5WgMXPgJ4EDPVmCETCBpJtQ/viewform)。

DEVINJPのソースコードを変更したい場合は、[Development.md](https://github.com/All-Hands-AI/DEVINJP/blob/main/Development.md)をご覧ください。

問題がありますか？[トラブルシューティングガイド](https://docs.all-hands.dev/modules/usage/troubleshooting)が役立ちます。

## 📖 ドキュメント

プロジェクトについてさらに学び、DEVINJPの使用に関するヒントを得るには、
[ドキュメント](https://docs.all-hands.dev/modules/usage/getting-started)をご覧ください。

そこでは、異なるLLMプロバイダーの使用方法、
トラブルシューティングリソース、高度な設定オプションに関するリソースが見つかります。

## 🤝 コミュニティへの参加方法

DEVINJPはコミュニティ主導のプロジェクトであり、誰からの貢献も歓迎します。私たちはほとんどのコミュニケーションを
Slackを通じて行っているため、ここから始めるのが最適ですが、DiscordやGithubでのご連絡も歓迎します：

- [Slackワークスペースに参加する](https://join.slack.com/t/devinjp-ai/shared_invite/zt-2ngejmfw6-9gW4APWOC9XUp1n~SiQ6iw) - ここでは研究、アーキテクチャ、将来の開発について話し合います。
- [Discordサーバーに参加する](https://discord.gg/ESHStjSjD4) - これは一般的な議論、質問、フィードバックのためのコミュニティ運営サーバーです。
- [Github Issuesを読んだり投稿したりする](https://github.com/All-Hands-AI/DEVINJP/issues) - 取り組んでいる課題を確認したり、自分のアイデアを追加したりできます。

コミュニティについての詳細は[COMMUNITY.md](./COMMUNITY.md)を、貢献に関する詳細は[CONTRIBUTING.md](./CONTRIBUTING.md)をご覧ください。

## 📈 進捗状況

月次のDEVINJPロードマップは[こちら](https://github.com/orgs/All-Hands-AI/projects/1)でご覧いただけます（毎月末のメンテナー会議で更新されます）。

<p align="center">
  <a href="https://star-history.com/#All-Hands-AI/DEVINJP&Date">
    <img src="https://api.star-history.com/svg?repos=All-Hands-AI/DEVINJP&type=Date" width="500" alt="Star History Chart">
  </a>
</p>

## 📜 ライセンス

MITライセンスの下で配布されています。詳細は[`LICENSE`](./LICENSE)をご覧ください。

## 🙏 謝辞

DEVINJPは多くの貢献者によって構築されており、すべての貢献に深く感謝しています！また、他のオープンソースプロジェクトの上に構築されており、それらの作業に深く感謝しています。

DEVINJPで使用されているオープンソースプロジェクトとライセンスのリストについては、[CREDITS.md](./CREDITS.md)ファイルをご覧ください。

## 📚 引用

```
@misc{devinjp,
      title={{DEVINJP: An Open Platform for AI Software Developers as Generalist Agents}},
      author={Xingyao Wang and Boxuan Li and Yufan Song and Frank F. Xu and Xiangru Tang and Mingchen Zhuge and Jiayi Pan and Yueqi Song and Bowen Li and Jaskirat Singh and Hoang H. Tran and Fuqiang Li and Ren Ma and Mingzhang Zheng and Bill Qian and Yanjun Shao and Niklas Muennighoff and Yizhe Zhang and Binyuan Hui and Junyang Lin and Robert Brennan and Hao Peng and Heng Ji and Graham Neubig},
      year={2024},
      eprint={2407.16741},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2407.16741},
}
```
