# coding: utf-8
from django.dispatch import Signal

result_received = Signal(["InvId", "OutSum"])
success_page_visited = Signal(["InvId", "OutSum"])
fail_page_visited = Signal(["InvId", "OutSum"])
