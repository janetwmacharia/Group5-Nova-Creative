from django.shortcuts import render

def home(request):

    services = [
        {
            'name': 'Web Development',
            'description': 'We create responsive, user-friendly websites that help businesses grow online.',
            'icon': 'bi-activity'
        },
        {
            'name': 'Graphic Design',
            'description': 'We design creative visuals and brand identities that make businesses stand out.',
            'icon': 'bi-bounding-box-circles'
        },
        {
            'name': 'Digital Marketing',
            'description': 'We help businesses reach their audiences through effective digital marketing strategies.',
            'icon': 'bi-calendar4-week'
        },
        {
            'name': 'Search Engine Optimization',
            'description': 'We improve website visibility and help businesses attract more visitors through search engines.',
            'icon': 'bi-broadcast'
        }
    ]

    return render(request, 'index.html', {'services': services})