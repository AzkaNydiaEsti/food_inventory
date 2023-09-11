from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Azka Nydia Estiningtyas',
        'class': 'PBP E',
        'item name': 'Adeptus Temptation',
        'item quality': '5-Star',
        'item type': 'ATK-Boosting Dishes',
        'item description': 'Increases all party members ATK by 260~372 and CRIT Rate by 8~12% for 300s.',
        'item amount': '2'
   
        
    }

    return render(request, "main.html", context)