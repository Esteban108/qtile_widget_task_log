from datetime import datetime
from pathlib import Path

from libqtile.widget import base


class TaskLog(base.InLoopPollText):
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ('format', 'minutes: {time}', 'Display format'),
        ('prompt_name', 'prompt', 'Prompt use for get the task text'),
        ('prompt_text', 'task: ', 'The text showing on prompt'),
        ('get_time', lambda start_date: round((datetime.now() - start_date).seconds / 60, 2),
         'function to get time; return int/float'),
        ('file_path', '~/tasks.log', 'The file path'),
        ('line_saved', '\nDate: {date}\tmin:{time}\ttask:{task}', 'Line saved to file when user input a task'),
        ('date_format', '%Y-%m-%d %H:%M', 'The date format to save on file'),
        ('update_interval', 1, 'The update interval.'),
    ]

    def __init__(self, **config):
        super().__init__(**config)
        self.add_defaults(TaskLog.defaults)

        self.start_date = datetime.now()
        if "~" in self.file_path:
            self.file_path = self.file_path.replace("~", str(Path.home()))

    def _start_input(self, task):
        with open(self.file_path, 'a') as A:
            A.write(self.line_saved.format(**{
                "date": datetime.now().strftime(self.date_format),
                "time": str(self.get_time(self.start_date)),
                "task": task
            }))
        self.start_date = datetime.now()

    def poll(self):
        return self.format.format(
            **{
                'time': str(self.get_time(self.start_date)),
            })

    def button_press(self, x, y, button):
        if button == 1:
            p = self.qtile.widgets_map[self.prompt_name]
            p.start_input(self.prompt_text, self._start_input)

    def tick(self):
        self.update(self.poll())
        return self.update_interval
