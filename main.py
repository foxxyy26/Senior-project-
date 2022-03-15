import mido 
mid = mido.MidiFile(' ', clip=True)
mid.tracks 

for m in mid.tracks[0][:20]:
  print(m)
  
for m in mid.tracks[2][:20]  
  print(m)
  
  for m in mid.tracks[3][:20]:
  print(m)
  for m in mid.tracks[4][:20]:
  print(m)
  
  def msg2dict(msg):
    result = dict()
    if 'note_on' in msg:
      on_ = True 
    elif 'note_off' in msg:
      on_ = False 
    else:
       on_ = None
     
    
  
