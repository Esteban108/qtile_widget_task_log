# TaskLog Widget

## About
A widget that allows you to log tasks in a file.

## Demo
![Screenshot](img/gif.gif?raw=true)

## Setup
```bash
pip install git+https://github.com/Esteban108/qtile_widget_task_log
```
```python
#  config.py
from libqtile.widget.prompt import Prompt
from task_log import TaskLog

#  ...

widgets_list = [
    Prompt(),
    TaskLog()
]
#  ...
```

## Parameters
TextBox base http://docs.qtile.org/en/latest/manual/ref/widgets.html#libqtile.widget.TextBox
### Customs
<table>
        <tr>
                <td><h4>Key</h4></td>
                <td><h4>Default</h4></td>
                <td><h4>description</h4></td>
        </tr>
<tr>
    <td> format</td>
    <td>minutes: {time}</td>
    <td>Display format</td>
</tr>

<tr>
    <td> prompt_name</td>
    <td>prompt</td>
    <td>Prompt use for get the task text</td>
</tr>

<tr>
    <td> prompt_text</td>
    <td>task:</td>
    <td>The text showing on prompt</td>
</tr>

<tr>
    <td> get_time</td>
    <td>lambda start_date: round((datetime.now() - start_date).seconds / 60, 1)</td>
    <td>function to get time; return int/float</td>
</tr>

<tr>
    <td> file_path</td>
    <td>~/tasks.log</td>
    <td>The file path</td>
</tr>

<tr>
    <td> line_saved</td>
    <td>\nDate: {date}\tmin:{time}\ttask:{task}</td>
    <td>Line saved to file when user input a task</td>
</tr>

<tr>
    <td> date_format</td>
    <td>%Y-%m-%d %H:%M</td>
    <td>The date format to save on file</td>
</tr>

<tr>
    <td> update_interval</td>
    <td>1</td>
    <td>The update interval.</td>
</tr>


</table>
 