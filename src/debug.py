"""
Copyright 2024 Rishav Chakraborty

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import datetime

class Debug:
    def __init__(self, debug_level: int = 1, store_log: bool = True):
        self.log_count: int = 0
        self.store_log: bool = store_log
        self.debug_level: int = debug_level
        if (store_log):
            self.output_log: str = 'START TIMESTAMP: ' + str(datetime.datetime.now()) + '\n'

    def log(self,  message: str, debug_level: int = 0):
        if (debug_level > self.debug_level): return
        self.log_count += 1
        if (self.store_log):
            self.output_log += f'TIMESTAMP: {datetime.datetime.now()}, DEBUG LEVEL {debug_level} LOG {self.log_count}: ' + message + '\n'
        print(f'DEBUG LOG {self.log_count}: ' + message)

    def write_log(self, file_path: str):
        if (not self.store_log):
            self.log('Logs are not being stored. Nothing to write.', 0)
        self.output_log += 'STOP TIMESTAMP: ' + str(datetime.datetime.now()) + '\n\n'
        print(self.output_log)
        with open(file_path, 'a', encoding = 'utf-8') as log_file:
            log_file.write(self.output_log)
