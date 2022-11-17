# PyProjects

色々なプロジェクト (Distribution) のインストールパターンを網羅する。

最初に venv を作成して有効化しておくことを推奨する:

```sh
python3 -m venv ./venv  # 一時的な環境
. ./venv/bin/activate
```

## Install from sdist

Create sdist:

```sh
python -m build --sdist
```

Install:

```sh
python -m pip install ./dist/project-0.0.0.tar.gz
```

## Install from git-archive

Create tar.gz:

```sh
git archive HEAD:contrib/project1 -o ./project1.tar.gz
```

If create zip:

```sh
git archive HEAD:contrib/project1 -o ./project1.zip
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
python -m pip install -U "project1 @ git+https://github.com/oshinko/pyprojects.git@main#subdirectory=contrib/project1"
```
