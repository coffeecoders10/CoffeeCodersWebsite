import json

data = {
'live_projects' : [
    {
        'name' : "Pictionary",
        'desc' : "The Game of Pictionary in a online medium",
        'img'  : 'images/menu-1.jpg',
        'link' : '/abc'
    },
    {
        'name' : "Pictionary2",
        'desc' : "The Game of Pictionary in a online medium",
        'img'  : 'images/menu-1.jpg',
        'link' : '/abc'
    },
    {
        'name' : "Pictionary3",
        'desc' : "The Game of Pictionary in a online medium",
        'img'  : 'images/menu-1.jpg',
        'link' : '/abc'
    }
    ],
'numbers' : {
    'years' : '2',
    'live' : '3',
    'total' : '10'
},
'git_projects' : [
    [
        {
            'name' : 'Japenese-English Translator',
            'desc' : 'Application that Converts Japanese text to English comprehension.',
            'topic' : 'Natural Language Processing',
            'link' : '/abcd',
            'icon' : 'fa fa-battery-full'
        },
        {
            'name' : 'Japenese-English Translator',
            'desc' : 'Application that Converts Japanese text to English comprehension.',
            'topic' : 'Natural Language Processing',
            'link' : '/abcd',
            'icon' : 'fa fa-battery-full'
        },
        {
            'name' : 'Japenese-English Translator',
            'desc' : 'Application that Converts Japanese text to English comprehension.',
            'topic' : 'Natural Language Processing',
            'link' : '/abcd',
            'icon' : 'fa fa-battery-full'
        },
        {
            'name' : 'Japenese-English Translator',
            'desc' : 'Application that Converts Japanese text to English comprehension.',
            'topic' : 'Natural Language Processing',
            'link' : '/abcd',
            'icon' : 'fa fa-battery-full'
        }
    ],
    [
        {
            'name' : 'Japenese-English Translator22',
            'desc' : 'Application that Converts Japanese text to English comprehension.',
            'topic' : 'Natural Language Processing',
            'link' : '/abcd',
            'icon' : 'fa fa-battery-full'
        },
        {
            'name' : 'Japenese-English Translator22',
            'desc' : 'Application that Converts Japanese text to English comprehension.',
            'topic' : 'Natural Language Processing',
            'link' : '/abcd',
            'icon' : 'fa fa-battery-full'
        },
        {
            'name' : 'Japenese-English Translator22',
            'desc' : 'Application that Converts Japanese text to English comprehension.',
            'topic' : 'Natural Language Processing',
            'link' : '/abcd',
            'icon' : 'fa fa-battery-full'
        },
        {
            'name' : 'Japenese-English Translator22',
            'desc' : 'Application that Converts Japanese text to English comprehension.',
            'topic' : 'Natural Language Processing',
            'link' : '/abcd',
            'icon' : 'fa fa-battery-full'
        }
    ]
],
'story' : {
    'desc' : 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
    'image' : 'images/big-logo.png',
},
'members' : [
    {
        'name' : 'Nitish Talekar',
        'desc' : 'MS in CS from NCSU',
        'img' : 'images/nitish-profile.jpg',
        'link' : 'nitishtalekar.pythonanywhere.com'
    },
    {
        'name' : 'Nitish Talekar',
        'desc' : 'MS in CS from NCSU',
        'img' : 'images/nitish-profile.jpg',
        'link' : 'nitishtalekar.pythonanywhere.com'
    }
],
'description' :{
    'addr' : 'India - USA',
    'mail' : 'coffeecoders10@gmail.com',
    'github' : 'link'
}
}

y = json.dumps(data, indent = 4)

with open("desc.json", "w") as outfile:
    json.dump(data, outfile, indent=4)
