# ВКР

Используется [этот tex шаблон](https://github.com/latex-g7-32/latex-g7-32) и [этот репозиторий](https://github.com/OsipXD/miet-thesis) с небольшими изменениями

[Результат](https://github.com/eqlion/bachelor-diploma/blob/main/build/main.pdf)

## Установка

Скачать последнюю версию.

Клонировать репозиторий:

```
git clone https://github.com/eqlion/bachelor-diploma.git
```

Скопировать файлы или лучше сделать мягкую ссылку:
`G2-105.sty`, `G7-32.cls`, `G7-32.sty`, `GostBase.clo`, `gosttitleGostRV15-110mipt.sty`, `gosttitleGostRV15-110.sty`, `local-minted.sty` в локальный texmf (`$HOME/texmf/`).
Проверить это можно командой `kpsewhich -var-value=TEXMFHOME`.
Относительно texmf путь будет `texmf/tex/latex/latex-g7-32/`.

```sh
mkdir -p $HOME/texmf/tex/latex/latex-g7-32/
ln -s tex/{G*|gosttitle*|local-minted.sty} $HOME/texmf/tex/latex/latex-g7-32/
```

(или просто оставить их в папке ./tex)

### Зависимости

##### LaTeX пакеты

```
cm-unicode-fonts minted polyglossia xecyr
```

<!-- ##### Программы
```
inkscape dia graphviz python pygmentize
``` -->

## Использование

Просто запустить файл `build.sh`. В результате работы в папке `build` будет создан файл `main.pdf`. Иногда нужно запустить билд ещё раз для библиографии и содержания.

### Редактор

Весь диплом пишется в VSCode с расширением [LaTeX workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop). Для создания библиографии для BiBtex по doi использовал https://doi2bib.org.

Более подробное описание, список авторов и т.д. - на странице стиля: https://github.com/latex-g7-32/latex-g7-32
