from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Azka Nydia Estiningtyas',
        'class': 'PBP E',
        'item_name': 'Adeptus Temptation',
        'quality': '5-Star',
        'type': 'ATK-Boosting Dishes',
        'description': 'Increases all party members ATK by 260~372 and CRIT Rate by 8~12 for 300s.',
        'amount': '2'
    }

    return render(request, "main.html", context)