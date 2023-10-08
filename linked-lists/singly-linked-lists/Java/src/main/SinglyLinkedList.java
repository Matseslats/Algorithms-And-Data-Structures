package main;

import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * A Singly Linked List
 * @author Mats Haugerud
 * @version 1.0, 06 October 2023
 */
public class SinglyLinkedList<E> implements List<E>{
    private Node<E> head;
    private Node<E> tail;
    private int listSize;
    public SinglyLinkedList(){
        head = null;
        tail = null;
        listSize = 0;
    }
    @Override
    public void addFirst(E element) {
        Node<E> newHead = new Node<>(element);
        newHead.setNext(head);
        head = newHead;
        if (listSize == 0){
            tail = head;
        }
        listSize += 1;
    }

    @Override
    public void addLast(E element) {
        Node<E> newTail = new Node<>(element);
        if (listSize == 0){
            tail = newTail;
            head = tail;
        } else {
            tail.setNext(newTail);
            tail = newTail;
        }
        listSize += 1;
    }

    @Override
    public E removeFirst() throws NoSuchElementException {
        Node<E> oldHead = head;
        if (head == null){
            throw new NoSuchElementException();
        }
        if (head.getNext() != null){
            head = head.getNext();
        } else {
            head = null;
        }
        listSize -= 1;
        return oldHead.getElement();
    }

    @Override
    public E removeLast() throws NoSuchElementException {
        if (head == null){
            throw new NoSuchElementException();
        }
        if (head == tail){ // There is only one element
            Node<E> toReturn = head;
            head = null;
            tail = null;
            listSize -= 1;
            return toReturn.getElement();
        }
        Node<E> current = head;
        Node<E> secondToLast = head;
        while (current.getNext() != null){
            secondToLast = current;
            current = current.getNext();
        }
        tail = secondToLast;
        tail.setNext(null);
        listSize -= 1;
        return current.getElement();
    }

    @Override
    public E getFirst() throws NoSuchElementException {
        if (head == null){
            throw new NoSuchElementException();
        }
        return head.getElement();
    }

    @Override
    public E getLast() throws NoSuchElementException {
        if (listSize == 0){
            throw new NoSuchElementException();
        }
        return tail.getElement();
    }

    @Override
    public boolean isEmpty() {
        return listSize == 0;
    }

    @Override
    public int getSize() {
        return listSize;
    }

    @Override
    public Iterator<E> iterator() {
        return new ForwardListIterator<E>(head);
    }
}
