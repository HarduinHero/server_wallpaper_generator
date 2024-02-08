# Generateur de fond d'écran pour serveur

Un script pour générer les fond d'écran des serveurs.

## Usage

Le script prend un fichier `data.json` qui associe l'image a prendre comme fond de base (nom dans le dossier background) et les champs à mettre sur le fond d'écran. Le fichier `data.model.json` peut servir de base pour un fichier data.json.

```json title="data.model.json"
[
    {
        "_champSansLabel" : {
            "txt" : "SERV-X",
            "size" : 50,
            "color" : [25, 150, 200]
        },
        "ip" : {
            "txt" : "192.168.X.X",
            "size" : 25
        },
        "__bg__" : "blank_b.png"
    }
]
```

Ici, on a des champs nommé par leur clés :

- `_champSansLabel` le nom de ce champs ne sera pas montré car il commence par un underscore (`_`).
- `ip` le nom de ce champs sera affiché sous la forme `"ip : ..."`.
- `__bg__` est un **champ obligatoire** qui contient seulement le nom de l'image de fond qui sera utilisé pour ce fond d'écran. Il sagit du nom de fichier, sans chemin. Le fichier doit se trouver dans le dossier background.

Les valeurs des champs (non `__bg__`) sont des objets qui doivent contenir

- Obligatoirement un champ `"txt"`.
- Optionnellement un champ `"color"` qui remplace la couleur par défaut, la valeur doit être une liste de valeurs décimales (ex:`[25, 150, 200]`).
- Optionnellement un champ `"size"` qui remplace la taille de police par défaut.

> Les valeurs constantes / par défaut sont déclarées dans le fichier ``const.py``.