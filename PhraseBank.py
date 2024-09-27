import random
class PhraseBank:
  def __init__(self,fname):
   self.phrases = {}
   with open(fname) as f:
      data = f.read().splitlines()
   for line in data:
      if line.startswith("**"):
        topic = line[2:].upper()
        self.phrases[topic] = []
      else:
        self.phrases[topic].append(line.upper())
  def next_phrase(self,topic):
    i = random.randint(0,len(self.phrases[topic]))
    return self.phrases[topic][i]
  def get_all_topics(self):
   return list(self.phrases.keys())