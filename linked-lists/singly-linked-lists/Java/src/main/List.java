package main;

import java.util.NoSuchElementException;

/**
 * A list interface.
 * @author Christine Zarges, Mats Haugerud
 * @version 2.1, 06 October 2023
 */
public interface List<E> extends Iterable<E> {
    /**
     * Adds a new element to the front of the list.
     *
     * @param element the element to be added
     */
    void addFirst(E element);

    /**
     * Adds a new element to the back of the list.
     *
     * @param element the element to be added
     */
    void addLast(E element);

    /**
     * Removes the element at the front of the list.
     *
     * @return the element at the front of the list
     * @throws NoSuchElementException if list is empty
     */
    E removeFirst() throws NoSuchElementException;

    /**
     * Removes the element at the back of the list.
     *
     * @return the element at the back of the list
     * @throws NoSuchElementException if list is empty
     */
    E removeLast() throws NoSuchElementException;

    /**
     * Get the element at the head of the list.
     *
     * @return the first element in the list
     * @throws NoSuchElementException if list is empty
     */
    E getFirst() throws NoSuchElementException;

    /**
     * Get the element at the tail of the list.
     *
     * @return the last element in the list
     * @throws NoSuchElementException if list is empty
     */
    E getLast() throws NoSuchElementException;

    /**
     * Determines if the list is empty.
     *
     * @return true if the list is empty, false otherwise
     */
    boolean isEmpty();

    /**
     * Determines the number of elements in the list
     *
     * @return the number of elements in the list
     */
    int getSize();
}
