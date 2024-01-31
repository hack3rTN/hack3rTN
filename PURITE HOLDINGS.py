# Fonction pour afficher une ligne de séparation
def print_separator():
    print('-' * 50)

# Fonction pour afficher les détails d'une section (achats ou dépenses)
def print_section(title, items):
    print_separator()
    print(f'{title.upper():^50}')
    print_separator()
    print('| Produit/Description             | Quantité/Montant | Prix unitaire   | Total           |')
    print_separator()
    for item in items:
        print(f'| {item["nom" if "nom" in item else "description"][:30]:<30} | {item["quantite" if "quantite" in item else "montant"]:^15} | ${item["prix_unitaire" if "prix_unitaire" in item else "montant"]:.2f}          | ${item["total" if "total" in item else "montant"]:.2f}         |')
    print_separator()

# Fonction pour calculer le total d'une section
def calculate_total(items):
    return sum(item["total" if "total" in item else "montant"] for item in items)

# Informations générales
nom_client = "PURITE HOLDINGS"
adresse_client = "123 Rue des Exemples, Villeville"
num_facture = "2022002"
date_facture = "2022-02-15"

# Achats
achats = [
    {"nom": "Produit PURITE HOLDINGS", "quantite": 2, "prix_unitaire": 50.0, "total": 100.0},
    {"nom": "PURITE HOLDINGS", "quantite": 1, "prix_unitaire": 30.0, "total": 30.0},
]

# Dépenses
depenses = [
    {"description": "Frais de livraison", "montant": 50.0},
    {"description": "Frais d'installation", "montant": 100.0},
]

# Affichage de la facture
print_separator()
print(f'{"FACTURE N° " + num_facture:^50}')
print_separator()

print(f'Client: {nom_client}, {adresse_client}')
print(f'Date: {date_facture:^50}\n')

# Affichage des détails des achats et calcul du total
print_section("DÉTAILS DES ACHATS", achats)
total_achats = calculate_total(achats)

# Affichage des détails des dépenses et calcul du total
print_section("DÉTAILS DES DÉPENSES", depenses)
total_depenses = calculate_total(depenses)

# Calcul du total de la facture
total_facture = total_achats + total_depenses

# Affichage du total de la facture
print_separator()
print(f'{"TOTAL FACTURE: $" + str(total_facture):^50}')
print_separator()
