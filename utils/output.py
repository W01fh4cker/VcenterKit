from datetime import datetime
from prettytable import PrettyTable

def output_format(level, text):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{current_time}]    [{level}]    {text}"

def output_simple_table(jsonstr, title, maxwidth):
    column_names = list(jsonstr.keys())
    row_data = list(jsonstr.values())
    output_tb = PrettyTable()
    output_tb.title = title
    output_tb.field_names = column_names
    output_tb.add_rows([row_data])
    output_tb.max_width = maxwidth
    output_tb_text = output_tb.get_string()
    return output_tb_text