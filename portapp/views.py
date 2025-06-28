from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    # -----------------------------------------------------------------------------------------------
    skil={'Python':'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg',
        #   'Python':'https://miro.medium.com/v2/resize:fit:1200/1*wpCkQ7PyQHMiUqgT1KbPZQ.png',
          'SQL':'https://pontia.tech/wp-content/uploads/2023/06/Imagen1.png',
          'Bootstarp':'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg',
        #   'Power BI':'https://www.solzit.com/wp-content/uploads/2024/05/microsoft-power-bi.png',
          'Django':'https://cdn.iconscout.com/icon/free/png-256/free-django-logo-icon-download-in-svg-png-gif-file-formats--technology-social-media-vol-2-pack-logos-icons-3029957.png',
          'HTML':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBd2rMcfI56SZEenhvautbZl_xUsPSHaktNw&s',
          'CSS':'https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/CSS3_logo.svg/2048px-CSS3_logo.svg.png',
          'JS':'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjNzNMC32aTaedQd9pA3RBNTZ6XLZtyiiZs2jM8vyF1U6OoFzwI9lkw4d93FFSNClw8yo&usqp=CAU',
          'React-JS':'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg',
          # 'React-JS':'https://cdn4.iconfinder.com/data/icons/logos-3/600/React.js_logo-512.png'
        }
    # ------------------------------------------------------------------------------------------------
    edu={'Secondary Education':['10 std','JSS English Medium High School','91.2% - 2018',1],
         'Pre-University Education':['PCMB','Jnanodaya PU College','78% - 2020',2],
         'Bachelor of Engineering':['Computer Science and Engineering','Government Engineering College, Kushalnagar','7.09 CGPA - 2024',3]         
        }
    # ------------------------------------------------------------------------------------------------
    proj=[
        {'projimg':1,'projdp':'images/DAT_dp.png','projtitle':'DAT','projdesc':'DAT is a multi-utility web app designed to simplify everyday tasks for users. It includes a Notes and 18 smart converters.','projqr':'images/DAT_qr.png','projlink':'https://dat-inf.vercel.app/'},
        {'projimg':1,'projdp':'images/qsprs.png','projtitle':'QSP Requirements','projdesc':"This Qspider's website  provides the details of the requirements and it's details. And also contains interview scheduled students list with info",'projqr':'','projlink':'https://github.com/Infinity-3/QSP_Requirements'},
        {'projimg':1,'projdp':'images/pbms.png','projtitle':'BMS','projdesc':'This project provides the info of the bikes. It is specific with company, that showcased the Showroom.','projqr':'','projlink':'https://github.com/Infinity-3/BMS'},
        {'projimg':1,'projdp':'images/pqsp.png','projtitle':"Qspider's Website",'projdesc':"This Qspider's Website provides details of courses and trainer's details of the Mysore branch.",'projqr':'','projlink':'https://github.com/Infinity-3/Qspider-Software-Training-Institute-Website'},
        {'projimg':0,'projdp':'https://www.svgrepo.com/show/11307/task-list.svg','projtitle':'Smart-Todo','projdesc':'A Todo-list where the list will be updated automatically according to the date given.','projqr':'','projlink':'https://github.com/Infinity-3/Smart-Todo'},
        # {'projimg':1,'projdp':'images/','projtitle':'','projdesc':'','projqr':'','projlink':''},
        # {'projimg':1,'projdp':'images/','projtitle':'','projdesc':'','projqr':'','projlink':''},
        # {'projimg':1,'projdp':'images/','projtitle':'','projdesc':'','projqr':'','projlink':''},
        # {'projimg':1,'projdp':'images/','projtitle':'','projdesc':'','projqr':'','projlink':''},
    ]
    # ------------------------------------------------------------------------------------------------
    # contact={'key':('image_link','link','anchor_name')}
    contact={'Whatsapp':('https://upload.wikimedia.org/wikipedia/commons/4/4c/WhatsApp_Logo_green.svg',"http://wa.me/+916360609733?text=Hi, I'm here.",'+91 6360609733'),
             'Gmail':('https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Gmail_icon_%282020%29.svg/1200px-Gmail_icon_%282020%29.svg.png','mailto:rajeshkoundinyan@gmail.com','rajeshkoundinyan@gmail.com'),
             'Github':('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/250px-GitHub_Invertocat_Logo.svg.png','https://github.com/Infinity-3','Infinity-3'),
             'Linkedin':('https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/800px-LinkedIn_icon.svg.png','https://www.linkedin.com/in/%E2%84%9C%CE%BB%E2%84%91-%E2%88%86-316354248/','ℜλℑ ∆'),
             'Resume':('https://static.vecteezy.com/system/resources/thumbnails/003/496/830/small/line-icon-for-resume-vector.jpg','https://drive.google.com/file/d/1eDaayU9iQZE3hN0uRklkMs9l7kPQ4GSz/view?usp=sharing','Resume'),
             'Phone':('https://i.pinimg.com/564x/8e/a0/83/8ea08365d331d8ae9bd93ba5f50528d4.jpg',"tel:+916360609733",'+91 6360609733'),
            }

    return render(request,'index.html',{'proj':proj,'edu':edu,'skil':skil,'contact':contact})

# def skills(request):
#     skil={'Python':'','SQL':'','Power BI':'','Django':'','HTML':'','CSS':'','JS':'','React-JS':''}
#     return render(request,'index.html',{'skil':skil})

# def education(request):
#     return render(request,'index.html')

# def projects(request):
#     proj=[
#         {'projdp':'','projtitle':'DAT','projdesc':'DAT','projqr':'','projlink':'https://dat-inf.vercel.app/'},
#         {'projdp':'','projtitle':'','projdesc':'','projqr':'','projlink':''},
#         # {'projdp':'','projtitle':'','projdesc':'','projqr':'','projlink':''}
#     ]
#     return render(request,'index.html',{'proj':proj})

# def contact(request):
#     contact={'Whatsapp':'','Gmail':'','Github':'','Linkedin':''}
#     return render(request,'index.html')

# def index(request):
#     return render(request,'index.html')

