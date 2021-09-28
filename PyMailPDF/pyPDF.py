from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.pagesizes import inch
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.validators import Auto

report = SimpleDocTemplate(
    "C:\\Users\\jcste\\googleAutomation\\pyAutomate\\pyMailPDF\\Report.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
table_data = []
fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}
for k, v in fruit.items():
    table_data.append([k, v])
print(table_data)
report_table = Table(data=table_data)
table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
# report.build([report_title, report_table])

report_pie = Pie(width=3*inch, height=3*inch)
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)
print(report_pie.data)
# [2, 5, 8, 3, 1, 1, 13]
print(report_pie.labels)
# ['apples', 'bananas', 'cherries', 'durians', 'elderberries', 'figs', 'grapes']

report_chart = Drawing()

report_chart.add(report_pie)
legend = Legend()
legend.alignment = 'right'
legend.x = 150
legend.y = 70
legend.colorNamePairs = Auto(obj=report_pie)
report_chart.add(legend)

report.build([report_title, report_table, report_chart])
