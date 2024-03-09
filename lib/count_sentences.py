#!/usr/bin/env python3
import re
class MyString:
  def __init__(self, value = ''):
    if not isinstance(value, str):
      print('The value must be a string.')
    self._value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, new_value):
    if not isinstance(new_value, str):
      print('The value must be a string.')
    self._value = new_value

  def is_sentence(self):
    return self._value.endswith('.')  
  
  def is_question(self):
    return self._value.endswith('?')  
  
  def is_exclamation(self):
    return self._value.endswith('!')

  def count_sentences(self):
    return len([sentence for sentence in re.split(r'[.!?]', self._value.strip()) if sentence])