
#!/usr/bin/env python
import os
import sys

sys.path.append(".\\DNP3_Decoder")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PowerDecoder.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

