# PyProjects

色々なプロジェクトのインストールパターンを網羅する。

最初に venv を作成して有効化しておくことを推奨する:

```sh
python3 -m venv ~/tmp/venv  # 一時的な環境
. ~/tmp/venv/bin/activate
```


## Install from archive

Create tar.gz:

```sh
git archive HEAD:sub/project1 -o ./project1.tar.gz
```

If create zip:

```sh
git archive HEAD:sub/project1 -o ./project1.zip
```

Install:

```sh
python -m pip install -U ./project1.tar.gz
```


## Install from Git over HTTP(S)

Install project:

```sh
python -m pip install -U "project @ git+https://github.com/oshinko/pyprojects.git@main"
```

Install only specific subprojects:

```sh
python -m pip install -U "project1 @ git+https://github.com/oshinko/pyprojects.git@main#subdirectory=sub/project1"
```
