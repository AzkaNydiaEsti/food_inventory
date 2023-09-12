from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Azka Nydia Estiningtyas',
        'class': 'PBP E',
        'item_name1': 'Adeptus Temptation',
        'quality1': '5-Star',
        'type1': 'ATK-Boosting Dishes',
        'description1': 'Increases all party members ATK by 260~372 and CRIT Rate by 8~12 for 300s.',
        'amount1': '2',
        'item_name2': 'Cream of Mushroom Soup',
        'quality2': '2-Star',
        'type2': 'Recovery Dishes',
        'description2': 'Revives a character and restores 250~550 HP.',
        'amount2': '1'
    }

    return render(request, "main.html", context)