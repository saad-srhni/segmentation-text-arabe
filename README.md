La segmentation de texte :
La segmentation fait partie du traitement automatique des langues
naturelles, Le principe est de segmenter un texte (une chaîne de caractères) en
paragraphes, mots, phrases et titres.
Cette opération est très sensible car une mauvaise segmentation entraine
des problèmes d'interprétation du texte. Chaque langue a ses spécificités à
prendre en compte.

Dans la langue française par exemple, bien que les espaces et les signes
de ponctuation délimitent souvent des phrases, certains délimiteurs peuvent
causer des ambiguïtés, Les caractères tels que «, », ″, ", “, ”, ‟, -, (, ), peuvent
délimiter des phrases comme ils peuvent délimiter des mots. Certain caractères
tels que "." ou "-" figurant dans des acronymes comme "P.V" ou "c’est-à-dire"
ne devront pas scinder ces derniers en deux ou plusieurs parties.

Présentation du Projet :
Le but du projet est de faire une recherche bibliographique sur les
algorithmes pour la segmentation de textes arabes, et implémenter ces
algorithmes en langage python.

Pour la réalisation d’un script Python qui permet de segmenter un texte en
arabes, on a utilisé la bibliothèque NLTK ,tashaphynen, naftawayh.
NLTK est une bibliothèque pour la création de programmes Python
utilisant des données en langage humain.

Naftawayh est une bibliothèque python pour le marquage de mots
arabes (classification de mots) en types (noms, verbes) .
tashaphyne est une bibliothèque python pour Extraction la racine de
mote .

Elle fournit des interfaces faciles à utiliser avec plus de 50 ressources
lexicales, ainsi qu’une suite de bibliothèques de traitement de texte pour la
classification, la création de jetons, l’arrêtage, le balisage, l’analyse et le
raisonnement sémantique, et un forum de discussion actif.
Grâce à un guide pratique présentant les bases de la programmation, des
sujets en linguistique informatique et une documentation complète sur les API,
NLTK convient aux linguistes, ingénieurs, étudiants, enseignants, chercheurs et
utilisateurs du secteur.

NLTK est un projet gratuit, à code source ouvert et piloté par la
communauté. Elle est disponible pour Windows, Mac OS X et Linux.

Implementation :
Ce projet est purement réalisé en langage Python et divisé en deux fichiers
d’extension .py :
 ProjetSegmentation.py :
Classe Segmenteur : Pour l’implémentation d’un segmenteur de texte.
+ Attribut :
- text : le contenu du fichier texte à segmenter.
+Methodes :
- __init__ : cette méthode lit le fichier en paramètre et affecte
son contenu à la variable text.
- segmenter_mots : cette méthode génère la liste des mots du
texte et l’affiche a la console et l’ecrit dans le fichier
output.txt
- segmenter_phrases : cette méthode génère la liste des
phrases du texte.
- segmenter_parags : cette méthode génère la liste des
paragraphes du texte.
 TestProjet.py :

Ce fichier contient une instance de la classe Segmenteur et l’appel à ses
différentes méthodes.
