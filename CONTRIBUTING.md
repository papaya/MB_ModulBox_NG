# Contribuer à MB_ModulBox_NG

Merci de contribuer aux documentations, sources KiCad et fichiers de fabrication du dépôt.

## Avant de proposer une modification

- Consultez le README du module et le statut des fichiers publiés dans le README racine.
- Pour un module standard, préservez l'attribution à Thorsten Klose et ucapps.de et distinguez clairement la ré-implémentation des sources amont.
- Pour un front-end, indiquez s'il s'agit d'une création MB MODULBOX NG ou d'une adaptation.
- N'ajoutez pas de fichiers de bibliothèque ou modèles 3D tiers sans vérifier leur provenance et les droits de redistribution.
- Le dépôt ne possède pas encore de fichier `LICENSE` : ne présentez pas une licence comme accordée et n'ajoutez pas de badge OSHWA avant clarification.

## Modifications KiCad

- Ouvrez et enregistrez le projet avec la version KiCad indiquée ou une version compatible.
- Conservez les placements et les liaisons existantes, sauf si la modification les vise explicitement.
- Évitez les chemins absolus machine/utilisateur dans les bibliothèques et modèles ; utilisez les variables KiCad ou des chemins relatifs portables.
- Joignez les rapports ERC/DRC et décrivez les violations nouvelles, corrigées ou préexistantes.
- Pour une modification de routage, comparez les résultats DRC avant/après et justifiez les changements de largeur, clearance et perçage.
- Ne marquez pas une carte « vérifiée » ou « prête à fabriquer » sans revue du schéma, PCB, Gerbers, BOM et contraintes d'alimentation.

## Documentation et fichiers de fabrication

- Mettez à jour le README du module avec son rôle, son brochage réellement vérifié, ses limites et les fichiers de fabrication disponibles.
- Les Gerbers, fichiers de perçage, BOM et positions doivent correspondre à la révision des sources KiCad.
- Mentionnez la version de KiCad et le fabricant/profil utilisé si les fichiers ont été testés.
- Préservez les données d'archive ; ne supprimez pas les anciens projets sans justification.

## Rapports et demandes

Utilisez les modèles GitHub pour les défauts matériels ou les nouvelles cartes. Pour un défaut, fournissez le projet, la révision, la version de KiCad, les rapports pertinents et une description reproductible. Ne joignez pas de données personnelles ou de secrets.
