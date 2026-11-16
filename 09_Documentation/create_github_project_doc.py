from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT=Path(r'E:/Data_Analysis/Dubai Automotive Intelligence Platform Sales, After-Sales & EV Adoption')
OUT=ROOT/'09_Documentation'/'Dubai_Automotive_Intelligence_GitHub_Description_Trilingual.docx'

def shade(cell, fill):
    tcPr=cell._tc.get_or_add_tcPr(); shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),fill); tcPr.append(shd)
def set_cell_text(cell,text,bold=False,color='FFFFFF'):
    cell.text=''; p=cell.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run(text); r.bold=bold; r.font.size=Pt(9); r.font.color.rgb=RGBColor.from_string(color); cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER

doc=Document(); sec=doc.sections[0]; sec.top_margin=Inches(.65); sec.bottom_margin=Inches(.65); sec.left_margin=Inches(.75); sec.right_margin=Inches(.75)
styles=doc.styles; styles['Normal'].font.name='Aptos'; styles['Normal'].font.size=Pt(10); styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'),'Aptos')
for name,size in [('Title',24),('Heading 1',17),('Heading 2',13)]: styles[name].font.name='Aptos Display'; styles[name].font.size=Pt(size); styles[name].font.color.rgb=RGBColor(0,0,0)

p=doc.add_paragraph(style='Title'); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.add_run('Dubai Automotive Intelligence Platform')
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run('GitHub Project Description and Portfolio Summary'); r.bold=True; r.font.color.rgb=RGBColor(0,102,177)
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.add_run('Amir Kargar — Data Analysis').italic=True

doc.add_heading('Project Overview',level=1)
doc.add_paragraph('This project is an end-to-end automotive intelligence platform designed for a Dubai automotive distributor such as Al-Futtaim Automotive. It transforms public market, vehicle, policy, customer-review and synthetic operational data into decision-ready analysis for sales, after-sales service, fleet operations and electric-vehicle adoption.')
doc.add_heading('What the Project Delivers',level=1)
for x in ['A traceable source registry covering official company, brand, government and public review sources.','A structured data model that connects Excel, SQL, Python, Power BI and an online dashboard.','Twenty practical business questions with charts, answers and management interpretation.','Synthetic operational tables for sales, inventory, service orders, CSAT, revenue and gross profit.','Forecast and service-risk demonstrations, clearly labelled as portfolio models.','Recommendations for EV adoption, charging infrastructure, after-sales quality and used-car transparency.']:
    doc.add_paragraph(x,style='List Bullet')
doc.add_heading('Technology Stack',level=1)
t=doc.add_table(rows=1,cols=4); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.style='Table Grid'
for c,h in zip(t.rows[0].cells,['Layer','Technology','Output','Purpose']): shade(c,'071B33'); set_cell_text(c,h,True)
for row in [('Data preparation','Excel / CSV','Master data','Cleaning and review'),('Database','SQL / SQLite','KPI queries','Reusable analytical model'),('Analysis','Python / Pandas / NumPy','Notebook and models','EDA, forecast and risk'),('BI','Power BI','Report specification','Executive reporting'),('Delivery','HTML / JavaScript','Online dashboard','Interactive stakeholder view')]:
    cells=t.add_row().cells
    for i,v in enumerate(row): cells[i].text=v; cells[i].vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER

doc.add_heading('Key Business Questions',level=1)
for x in ['Which brands and powertrains have the strongest portfolio coverage?','How should the company sequence EV and Hybrid adoption?','Where are the likely after-sales service and customer-experience gaps?','How can inventory, fleet and charging utilization be monitored?','Which actions should management prioritize in the next 90 days?']:
    doc.add_paragraph(x,style='List Bullet')
doc.add_heading('Important Data Note',level=1)
doc.add_paragraph('Public product, policy and review facts are source-traceable. Operational sales, inventory and service files labelled synthetic_ are demonstration data created for portfolio modelling and must be replaced with authorized company exports before real decisions.')
doc.add_heading('Online Dashboard',level=1)
doc.add_paragraph('https://dubai-auto-20q-intelligence.masoudkargar.chatgpt.site')

doc.add_page_break(); doc.add_heading('English Version',level=1)
doc.add_paragraph('I built an end-to-end automotive intelligence platform for the Dubai market. The project combines Excel, SQL, Python, Power BI-ready data and an interactive online dashboard. It analyzes vehicle portfolios, EV and Hybrid adoption, UAE policy targets, after-sales service quality, fleet operations, customer reviews and inventory decisions. The platform answers twenty practical business questions and translates the results into management recommendations. Public facts are source-traceable, while operational files are clearly labelled synthetic demonstrations. My goal is to show how I turn fragmented data into a clear business decision and a repeatable analytical pipeline.')

doc.add_heading('Arabic Version',level=1)
pa=doc.add_paragraph(); pa.alignment=WD_ALIGN_PARAGRAPH.RIGHT; pa.add_run('قمت ببناء منصة متكاملة لذكاء الأعمال وتحليل قطاع السيارات في سوق دبي. تجمع المنصة بين Excel وSQL وPython وPower BI ولوحة معلومات تفاعلية على الإنترنت. يحلل المشروع مجموعة السيارات، وانتشار السيارات الكهربائية والهجينة، وأهداف دولة الإمارات، وجودة خدمات ما بعد البيع، وإدارة الأساطيل، وآراء العملاء، وقرارات المخزون. يجيب المشروع عن عشرين سؤالاً عملياً ويحوّل النتائج إلى توصيات إدارية قابلة للتنفيذ. تم توثيق مصادر البيانات العامة، بينما تم تمييز البيانات التشغيلية التجريبية بوضوح على أنها بيانات اصطناعية لأغراض العرض والمحاكاة. الهدف هو توضيح قدرتي على تحويل البيانات المتفرقة إلى قرارات تجارية واضحة ومنهج تحليلي قابل للتكرار.')

doc.add_heading('نسخه فارسی',level=1)
pf=doc.add_paragraph(); pf.alignment=WD_ALIGN_PARAGRAPH.RIGHT; pf.add_run('من یک پلتفرم کامل هوش تجاری برای تحلیل بازار خودرو در دبی ساخته‌ام. این پروژه از Excel، SQL، Python، داده‌های آماده Power BI و یک داشبورد آنلاین تعاملی استفاده می‌کند. در این پروژه سبد خودروها، رشد خودروهای برقی و هیبریدی، اهداف سیاستی امارات، کیفیت خدمات پس از فروش، عملیات فلیت، نظرات مشتریان و تصمیم‌های موجودی تحلیل شده‌اند. پروژه به ۲۰ سؤال کاربردی کسب‌وکار پاسخ می‌دهد و نتایج را به پیشنهادهای مدیریتی قابل اجرا تبدیل می‌کند. داده‌های عمومی دارای منبع مشخص هستند و داده‌های عملیاتی با برچسب synthetic برای نمایش مدل تحلیلی ساخته شده‌اند. هدف من نشان‌دادن توانایی تبدیل داده‌های پراکنده به تصمیم تجاری و ساخت یک مسیر تحلیلی قابل تکرار است.')

doc.add_heading('Suggested GitHub Tags',level=1)
doc.add_paragraph('Automotive Analytics  |  Dubai Market  |  EV Adoption  |  After-Sales  |  SQL  |  Python  |  Power BI  |  Business Intelligence  |  Data Analysis')
doc.save(OUT); print(OUT)
