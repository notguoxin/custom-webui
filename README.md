> [!WARNING]  
> Not tested for production use. \
> May introduce bugs that is not present in the original [Open WebUI](https://github.com/open-webui/open-webui). \
> You can however file a [issue](https://github.com/notguoxin/custom-webui/labels)[^1]

# Custom WebUI 👋
A heavily simplified version of [Open WebUI](https://github.com/open-webui/open-webui)

# Version
check [here](VERSION.md) for more info

# What's removed/changed/added?
- Repository:
    - Removed Docker, pypi, frontend and backend build and formating[^2]
    - Modified realease github action
    - and more!
- Test/Debug:
    - Removed cypress test
    - and more!
- WebUI:
    - Removed RAG
    - Removed Community rating
    - Removed File uploading
    - Removed web search functionality
    - Removed API functionality
    - Removed LDAP functionality
    - Removed Chat sharing
    - Removed OAuth
    - Removed Voice
    - Removed Valves
    - Removed Tools
    - Removed Channels
    - Removed Functions
    - Removed Playground
    - Removed Pipelines
    - and more!

## License 📜

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details. 📄

---

Created by [Timothy Jaeryang Baek](https://github.com/tjbck) - Let's make Open WebUI even more amazing together! 💪 \
Modified by [NotGuoXin](https://github.com/notguoxin)

---
## Foodnotes
[^1]: I may or may not have time to fix the issue, look out for labels like: `wontfix`, `on halt`.

[^2]: However you can download and install using pip from getting the whl file from the release page
    > `pip install open-webui-VERSION-py3-none-any.whl`