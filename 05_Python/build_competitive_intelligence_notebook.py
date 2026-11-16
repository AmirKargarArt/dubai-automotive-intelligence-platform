import json
from pathlib import Path
root=Path(r'E:/Data_Analysis/Dubai Automotive Intelligence Platform Sales, After-Sales & EV Adoption')
cells=[]
def md(x): cells.append({'cell_type':'markdown','metadata':{},'source':x.splitlines(True)})
def code(x): cells.append({'cell_type':'code','execution_count':None,'metadata':{},'outputs':[],'source':x.splitlines(True)})
md('# UAE Automotive Competitive Intelligence\n## Al-Futtaim Automotive vs Key Competitors\n**Amir Kargar — Data Analysis**')
code("""import pandas as pd\nimport matplotlib.pyplot as plt\nfrom pathlib import Path\nROOT=Path(r'E:/Data_Analysis/Dubai Automotive Intelligence Platform Sales, After-Sales & EV Adoption'); C=ROOT/'02_Data_Clean'\nbenchmark=pd.read_csv(C/'competitor_public_benchmark.csv'); score=pd.read_csv(C/'competitor_scorecard.csv')\nplt.style.use('seaborn-v0_8-whitegrid'); display(benchmark); display(score)\n""")
items=[('امتیاز کل رقبا','total_score','امتیاز کل','امتیاز ساختاریافته است و جایگزین سهم بازار حسابرسی‌شده نیست.'),('آمادگی EV','ev_readiness','آمادگی EV','تعداد مدل EV کافی نیست و باید شارژ، تکنسین و قطعات هم اضافه شوند.'),('خدمات و فلیت','service_fleet','خدمات و فلیت','این ترکیب برای مشتریان B2B و حفظ مشتری مهم است.'),('تجربه دیجیتال','digital_experience','تجربه دیجیتال','مسیر مجازی تا تست‌درایو و رزرو سرویس باید اندازه‌گیری شود.'),('پوشش برند','brand_count','تعداد برندها','پوشش برند مزیت است اما پیچیدگی عملیات را بالا می‌برد.'),('توانمندی خودروهای دست‌دوم','used_cars','خودروهای دست‌دوم','بازرسی، گارانتی و تأمین مالی عامل اصلی رقابت هستند.'),('مراکز خدمات','service_center_count','مراکز خدمات','تعداد مرکز باید با ظرفیت و زمان انتظار ترکیب شود.'),('فلیت و موبیلیتی','fleet_mobility','فلیت و موبیلیتی','فلیت و اجاره برای تحلیل B2B اهمیت دارد.'),('پورتفولیو','portfolio_breadth','پورتفولیو','تنوع سبد باید با سهم فروش و حاشیه سود سنجیده شود.'),('شکاف رقابتی','score_vs_average','امتیاز نسبت به میانگین','شکاف‌ها باید با داده شعب و سهم بازار اعتبارسنجی شوند.')]
for q,col,title,analysis in items:
    md('## '+q)
    if col=='service_fleet': c="""score['service_fleet']=score.after_sales+score.fleet_mobility\nx=score.sort_values('service_fleet'); x.plot.barh(x='company',y='service_fleet',legend=False,title='Q3 خدمات و فلیت'); plt.show()\nprint('تحلیل: '+%r)"""%analysis
    elif col=='score_vs_average': c="""score['score_vs_average']=score.total_score-score.total_score.mean()\nx=score.sort_values('score_vs_average'); x.plot.barh(x='company',y='score_vs_average',legend=False,title='Q10 شکاف از میانگین'); plt.show()\nprint('تحلیل: '+%r)"""%analysis
    elif col=='service_center_count': c="""x=benchmark.dropna(subset=['service_center_count']).sort_values('service_center_count'); x.plot.barh(x='company',y='service_center_count',legend=False,title='Q7 مراکز خدمات'); plt.show()\nprint('تحلیل: '+%r)"""%analysis
    else: c="""x=score.sort_values(%r); x.plot.barh(x='company',y=%r,legend=False,title=%r); plt.show()\nprint('تحلیل: '+%r)"""%(col,col,title,analysis)
    code(c)
md('## نتیجه\nAW Rostamani نزدیک‌ترین benchmark عمومی است. گام بعدی اتصال امتیازها به داده واقعی شعب، فروش، review و ظرفیت خدمات است.\n\n**Amir Kargar — Data Analysis**')
nb={'cells':cells,'metadata':{'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'}},'nbformat':4,'nbformat_minor':5}
out=root/'05_Python'/'Competitive_Intelligence_Analysis.ipynb'
out.write_text(json.dumps(nb,ensure_ascii=False,indent=1),encoding='utf-8')
print(out)
