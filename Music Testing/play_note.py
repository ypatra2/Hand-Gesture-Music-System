from scamp import *

session = Session()

piano = session.new_part("Piano")
# piano2 = session.new_part("Piano")

pitch = 64


# def piano_part(which_piano):
#     while True:
#         for pitch in pitches:
#             which_piano.play_note(pitch, 1.0, 0.0625)


piano.play_note(pitch, 100, 1)

# clock1 = session.fork(piano_part, args=(piano1,), initial_tempo=100)
# clock2 = session.fork(piano_part, args=(piano2,), initial_tempo=98)

# session.start_transcribing(clock=clock1)
# session.wait(30)

# performance = session.stop_transcribing()
# performance.to_score(QuantizationScheme.from_time_signature("3/4", 16)).show_xml()
