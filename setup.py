import setuptools 

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot_plugin_chatGPT_openai",
    version="0.0.4",
    author="schwarzwald",
    description="This is a QQ bot on chatGPT3 APT, but it does not support contextual replies.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Reversedeer/nonebot_plugin_chatGPT_openai",
    project_urls={
        "Bug Tracker": "https://github.com/Reversedeer/nonebot_plugin_chatGPT_openai/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires = [
        'nonebot-adapter-onebot>=2.0.0-beta.1',
        'nonebot2>=2.0.0-beta.1',
    ]
)