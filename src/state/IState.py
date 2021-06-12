#!/usr/bin/env python


import abc


class IState(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def entry(self):
        raise NotImplementedError(
            "users must define 'entry' to use this base class")

    @abc.abstractmethod
    def do(self):
        raise NotImplementedError(
            "users must define 'do' to use this base class")

    @abc.abstractmethod
    def exit(self):
        raise NotImplementedError(
            "users must define 'exit' to use this base class")

    @abc.abstractmethod
    def next(self):
        raise NotImplementedError(
            "users must define 'next' to use this base class")

    @abc.abstractmethod
    def event(self):
        raise NotImplementedError(
            "users must define 'event' to use this base class")
