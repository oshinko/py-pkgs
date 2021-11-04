# py-pkgs

## install from archive

tar.gz:

```sh
git archive HEAD:pkg1 -o ./pkg1.tar.gz
```

zip:

```sh
git archive HEAD:pkg1 -o ./pkg1.zip
```

install:

```sh
python -m pip install -U ./pkg1.tar.gz
```
