# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 22:03:44 2019

@author: fraal
"""

from chatterbot import ChatBot

chatbot = ChatBot(
        "Ejemplo Bot",
        trainer = "chatterbot.trainers.ChatterBotCorpusTrainer"
        )

chatbot.train(
        "chatterbot.corpus.spanish"
        )