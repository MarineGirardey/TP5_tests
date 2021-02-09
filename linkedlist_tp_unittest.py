#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:54:03 2021
@author: Marine Girardey
"""

class Node:
    """Node class for a linked list
    Attributes
    ----------
    param_data : int
    link : node.Node
    """
    def __init__(self, data):
        """Class constructor
        Parameters
        ----------
        param_data : int
            the data
        Returns
        -------
        None
            Node object
        """
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    """LinkedList class to create a linked list
    Attributes
    ----------
    param_data : any
    """
    def __init__(self, nodes=None):
        """Class constructor
        Parameters
        ----------
        data : any
            The value of the given node.
        Returns
        -------
        None
            A class instance.
        """
        self.head = None
        if nodes is not None and len(nodes) != 0:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def get(self, index):
        """
        get the index of each node and print the node of a given index
        Parameters
        ----------
        index : index of a node
        """
        if self.head is None:
            raise Exception('Node vide')
        else:
            return self.leonardo_recurs(index, self.head)

    def leonardo_recurs(self, index, node):
        """
        recursive function to browse each node until index is not equal to 0
        Parameters
        ----------
        index : the wanted index enter from the get function
        node : the node corresponding to a specific index
        """
        print(index, node)
        if node is None:
            return node
        if index == 0:
            return node
        else:
            return self.leonardo_recurs(index - 1, node.next)

    def add_after(self, data, new_node):
        """
        insert a new node after the node with the value == data
        Parameters
        ----------
        data : searched data
        new_node : node to insert
        """
        if not self.head:
            raise Exception("List is empty")
        for node in self:
            if node.data == data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data '{}' not found".format(data))

    def add_before(self, data, new_node):
        """
        insert a new node before the node with the value == data
        Parameters
        ----------
        data : searched data
        new_node : node to insert
        """
        if not self.head:
            raise Exception("List is empty")
        if self.head.data == data:
            return self.add_first(new_node)
        prev_node = self.head
        for node in self:
            if node.data == data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception("Node with data '{}' not found".format(data))

    def remove_node(self, data):
        """
        delete all node(s) value == data
        Parameters
        ----------
        data : searched data to delete
        """
        if not self.head:
            raise Exception("List is empty")
        if self.head.data == data:
            self.head = self.head.next
            return
        previous_node = self.head
        for node in self:
            if node.data == data:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception("Node with data '{}' not found".format(data))

    def add_first(self, node_to_add):
        """
        insert a node as the first node of the linkedlist
        Parameters
        ----------
        node_to_add : node to insert
        """
        node_to_add.next = self.head
        self.head = node_to_add

    def add_last(self, node_to_add):
        """
        insert a node as the last one of the linkedlist
        Parameters
        ----------
        node_to_add : node to insert
        """
        if self.head == None:
            self.head = node_to_add
            return
        node = self.head
        # while node.next is not None:*
        while node.next is not None:
            node = node.next
        node.next = node_to_add

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        #return "a"
        return "{}".format(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
            