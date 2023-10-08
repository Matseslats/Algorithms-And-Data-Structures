package main;

import java.util.NoSuchElementException;

/**
 * A Node
 * @author Mats Haugerud
 * @version 1.0, 06 October 2023
 */
public class Node<E> { // Lets user use any non-primitive type in <>
    private E element; // E gets replaced with type user used
    private Node<E> next;

    public E getElement() {
        if (element == null){
            throw new NoSuchElementException();
        }
        return element;
    }

    public void setElement(E element) {
        this.element = element;
    }

    public Node<E> getNext() {
        return next;
    }

    public void setNext(Node<E> next) {
        this.next = next;
    }

    public Node(E element) {
        this.element = element;
        next = null;
    }
}
