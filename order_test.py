# Божко Алексей_8а Марс — Финальный проект. Инженер по тестированию плюс

import sender_request

def positive_assert(track_order):
    order_response = sender_request.get_treck_order(track_order)
    assert order_response.status_code ==200

def test_get_order_on_track():
    positive_assert(sender_request.track_order)