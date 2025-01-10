> [!WARNING]  
> Not tested for production use. \
> May introduce bugs that is not present in the original [Open WebUI](https://github.com/open-webui/open-webui). \
> You can however file a [issue](https://github.com/notguoxin/custom-webui/labels)[^1]

# Custom WebUI 👋
> A heavily simplified version of [Open WebUI](https://github.com/open-webui/open-webui)

# Info:
- Main branch: 
    - [Latest release: ![GitHub Release](https://img.shields.io/github/v/release/notguoxin/custom-webui)](https://github.com/notguoxin/custom-webui/releases/latest/)
    - Release workflow: [![Release](https://github.com/notguoxin/custom-webui/actions/workflows/build-release.yml/badge.svg?branch=main)](https://github.com/notguoxin/custom-webui/actions/workflows/build-release.yml) 
- Dev branch:
    - Testing workflow: [![Test](https://github.com/notguoxin/custom-webui/actions/workflows/test-realease.yml/badge.svg?branch=dev)](https://github.com/notguoxin/custom-webui/actions/workflows/test-realease.yml)
    - ![GitHub commits since latest release (branch)](https://img.shields.io/github/commits-since/notguoxin/custom-webui/latest/dev)


# Version information:
> Check [here](VERSION.md) for more info

# What's removed/modified/added?
- Repository:
    - [Removed Docker build](https://github.com/notguoxin/custom-webui/commit/0579a275b904897ff5642c3a1e5c7dc642e9b5d6)
    - [Removed pypi build](https://github.com/notguoxin/custom-webui/commit/9c6dd2f057d00f4a4a4e8ffaae5fc73430946a29) [^2]
    - [Removed frontend and backend build and formating](https://github.com/notguoxin/custom-webui/commit/c0afcda2c4c2f3ade5fb608a6cb2aca97d7cf28a)
    - Modified realease github action
    - and more!
- Test/Debug:
    - [Removed cypress test](https://github.com/notguoxin/custom-webui/commit/9bb4ad7c164f3c3a462e670b9561c5700f75d390)
    - and more!
- WebUI:
    - Removed RAG[^3]
    - Removed Community rating[^3]
    - Removed File uploading[^3]
    - Removed web search functionality[^3]
    - [Removed API functionality](https://github.com/notguoxin/custom-webui/commit/75437d74a14ec6ec27e170f2443cc0a5cf93f922)
    - [Removed LDAP functionality](https://github.com/notguoxin/custom-webui/commit/252886932edb5538ab891949fb7f24c7b37378ed)
    - [Removed Chat sharing](https://github.com/notguoxin/custom-webui/commit/69f0630a8eef42f478a297803316cea2ed8a1bf3)
    - [Removed OAuth](https://github.com/notguoxin/custom-webui/commit/c9803f2736a5ee5642470af7edb46e4ed3429512)
    - [Removed Voice](https://github.com/notguoxin/custom-webui/commit/530a7a405998ff1d133a6578d0f0e9239132fc73)
    - [Removed Valves](https://github.com/notguoxin/custom-webui/commit/005c86d2d38f66ada22c009706c0dd62273809b9)
    - [Removed Tools](https://github.com/notguoxin/custom-webui/commit/46d5e8ae2a88ebd22cfc5fdd492b28e9760cf5dd)
    - [Removed Channels](https://github.com/notguoxin/custom-webui/commit/ba1e160c31b01f2f6079d143ec19328bcea43b3d)
    - Removed Functions[^3]
    - [Removed Playground](https://github.com/notguoxin/custom-webui/commit/0c2a884520447e5ef6f46d668184a836c2ca0380)
    - Removed Pipelines[^3]
    - [Removed Some of Advanced Params](https://github.com/notguoxin/custom-webui/commit/8458da49f2e680bb512012b431fd83dfbfe0dd30)
    - and more!

## License 📜

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details. 📄

---

Created by [Timothy Jaeryang Baek](https://github.com/tjbck) - Let's make Open WebUI even more amazing together! 💪 \
Modified by [NotGuoXin](https://github.com/notguoxin)

[^1]: I may or may not have time to fix the issue, look out for labels like: `wontfix`, `on halt`, `fixing`.

[^2]: However you can download and install using pip from getting the whl file from the release page
    > `pip install open-webui-VERSION-py3-none-any.whl`

[^3]: I don't know when did I remove it ¯\\_(ツ)_/¯