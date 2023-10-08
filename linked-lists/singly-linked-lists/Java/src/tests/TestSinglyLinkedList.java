package tests;

import main.ForwardListIterator;
import main.List;
import main.SinglyLinkedList;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import java.util.Iterator;
import java.util.NoSuchElementException;

import static org.junit.jupiter.api.Assertions.*;

public class TestSinglyLinkedList {
    private List<String> list;

    @BeforeEach
    public void setUp() {
        list = new SinglyLinkedList<>();
    }

    @Test
    @DisplayName("Iterator on empty list.")
    public void testIteratorInit () {
        Iterator<String> iterator = list.iterator();

        assertTrue(iterator instanceof ForwardListIterator, "Method iterator() must return ForwardListIterator object.");
        assertFalse(iterator.hasNext(), "Iterator on empty list must return false for hasNext() method.");
    }

    @Test
    @DisplayName("Empty list properties.")
    public void testEmptyList () {
        assertEquals(0, list.getSize(), "Size of empty list must be 0.");
        assertTrue(list.isEmpty(), "Method isEmpty() must return true for an empty list.");
    }

    @Test
    @DisplayName("Removing from empty list.")
    public void testRemoveFromEmptyList () {
        assertThrows(NoSuchElementException.class, () -> list.removeFirst(),
                "Throw an NoSuchElementException if user tries to remove the first element from an empty list.");
        assertThrows(NoSuchElementException.class, () -> list.removeLast(),
                "Throw an NoSuchElementException if user tries to remove the last element from an empty list.");
    }

    @Test
    @DisplayName("Getting elements from empty list.")
    public void testGetFromEmptyList () {
        assertThrows(NoSuchElementException.class, () -> list.getFirst(),
                "Throw an NoSuchElementException if user tries to retrieve the first element from an empty list.");
        assertThrows(NoSuchElementException.class, () -> list.getLast(),
                "Throw an NoSuchElementException if user tries to retrieve the last element from an empty list.");
    }

    @Test
    @DisplayName("Add one element at head.")
    public void testAddOneHead() {
        list.addFirst("1");

        // get methods
        assertEquals("1", list.getFirst(), "Head must reference inserted element.");
        assertEquals("1", list.getLast(),    "Tail must reference inserted element.");

        // properties
        assertEquals(1, list.getSize(), "Size of list must be 1.");
        assertFalse(list.isEmpty(), "Method isEmpty() must return false for a list of size 1.");

        // iterator
        Iterator<String> iterator = list.iterator();
        assertTrue(iterator.hasNext(), "Iterator must return true for hasNext() method.");
        assertEquals("1", iterator.next(), "Iterator must return inserted element.");
        assertFalse(iterator.hasNext(), "Iterator must return false for hasNext() method.");
    }

    @Test
    @DisplayName("Add one element at tail.")
    public void testAddOneTail() {
        list.addLast("1");

        // get methods
        assertEquals("1", list.getFirst(), "Head must reference inserted element.");
        assertEquals("1", list.getLast(),    "Tail must reference inserted element.");

        // properties
        assertEquals(1, list.getSize(), "Size of list must be 1.");
        assertFalse(list.isEmpty(), "Method isEmpty() must return false for a list of size 1.");

        // iterator
        Iterator<String> iterator = list.iterator();
        assertTrue(iterator.hasNext(), "Iterator must return true for hasNext() method.");
        assertEquals("1", iterator.next(), "Iterator must return inserted element.");
        assertFalse(iterator.hasNext(), "Iterator must return false for hasNext() method.");
    }

    @Test
    @DisplayName("Add two elements at front.")
    public void testAddTwoHead () {
        list.addFirst("1");
        list.addFirst("2");

        // get methods
        assertEquals("2", list.getFirst(), "First element in list incorrect.");
        assertEquals("1", list.getLast(), "Last element in list incorrect.");

        // properties
        assertEquals(2, list.getSize(), "Size of list must be 2.");
        assertFalse(list.isEmpty(), "Method isEmpty() must return false for a list of size 2.");

        // iterator
        Iterator<String> iterator = list.iterator();
        assertTrue(iterator.hasNext(), "Iterator must return true for hasNext() method.");
        assertEquals("2", iterator.next(), "First element in list incorrect.");
        assertEquals("1", iterator.next(), "Second element in list incorrect.");
        assertFalse(iterator.hasNext(), "Iterator must return false for hasNext() method.");
    }

    @Test
    @DisplayName("Add two elements at tail.")
    public void testAddTwoTail () {
        list.addLast("1");
        list.addLast("2");

        // get methods
        assertEquals("1", list.getFirst(), "First element in list incorrect.");
        assertEquals("2", list.getLast(), "Last element in list incorrect.");

        // properties
        assertEquals(2, list.getSize(), "Size of list must be 2.");
        assertFalse(list.isEmpty(), "Method isEmpty() must return false for a list of size 2.");

        // iterator
        Iterator<String> iterator = list.iterator();
        assertTrue(iterator.hasNext(), "Iterator must return true for hasNext() method.");
        assertEquals("1", iterator.next(), "First element in list incorrect.");
        assertEquals("2", iterator.next(), "Second element in list incorrect.");
        assertFalse(iterator.hasNext(), "Iterator must return false for hasNext() method.");
    }

    @Test
    @DisplayName("Add three elements at front.")
    public void testAddThreeHead () {
        list.addFirst("1");
        list.addFirst("2");
        list.addFirst("3");

        // get methods
        assertEquals("3", list.getFirst(), "First element in list incorrect.");
        assertEquals("1", list.getLast(), "Last element in list incorrect.");

        // properties
        assertEquals(3, list.getSize(), "Size of list must be 3.");
        assertFalse(list.isEmpty(), "Method isEmpty() must return false for a list of size 3.");

        // iterator
        Iterator<String> iterator = list.iterator();
        assertTrue(iterator.hasNext(), "Iterator must return true for hasNext() method.");
        assertEquals("3", iterator.next(), "First element in list incorrect.");
        assertEquals("2", iterator.next(), "Second element in list incorrect.");
        assertEquals("1", iterator.next(), "Third element in list incorrect.");
        assertFalse(iterator.hasNext(), "Iterator must return false for hasNext() method.");
    }

    @Test
    @DisplayName("Add three elements at tail.")
    public void testAddThreeTail () {
        list.addLast("1");
        list.addLast("2");
        list.addLast("3");

        // get methods
        assertEquals("1", list.getFirst(), "First element in list incorrect.");
        assertEquals("3", list.getLast(), "Last element in list incorrect.");

        // properties
        assertEquals(3, list.getSize(), "Size of list must be 3.");
        assertFalse(list.isEmpty(), "Method isEmpty() must return false for a list of size 3.");

        // iterator
        Iterator<String> iterator = list.iterator();
        assertTrue(iterator.hasNext(), "Iterator must return true for hasNext() method.");
        assertEquals("1", iterator.next(), "First element in list incorrect.");
        assertEquals("2", iterator.next(), "Second element in list incorrect.");
        assertEquals("3", iterator.next(), "Third element in list incorrect.");
        assertFalse(iterator.hasNext(), "Iterator must return false for hasNext() method.");
    }

    @Test
    @DisplayName("Add three elements and remove from front.")
    public void testAddThreeRemoveFromFront () {
        list.addFirst("1");
        list.addFirst("2");
        list.addFirst("3");

        // remove first element from front
        assertEquals("3", list.removeFirst(), "First element in list incorrect.");

        // properties
        assertEquals(2, list.getSize(), "Size of list must be 2.");
        assertFalse(list.isEmpty(), "Method isEmpty() must return false for a list of size 2.");

        // iterator over remaining list
        Iterator<String> iterator = list.iterator();
        assertTrue(iterator.hasNext(), "Iterator must return true for hasNext() method.");
        assertEquals("2", iterator.next(), "First element in list incorrect.");
        assertEquals("1", iterator.next(), "Second element in list incorrect.");
        assertFalse(iterator.hasNext(), "Iterator must return false for hasNext() method.");

        // remove remaining elements from front
        assertEquals("2", list.removeFirst(), "Second element in list incorrect.");
        assertEquals("1", list.removeFirst(), "Third element in list incorrect.");

        // check that list is now empty
        assertEquals(0, list.getSize(), "Size of list must be 0.");
        assertTrue(list.isEmpty(), "Method isEmpty() must return true for an empty list.");

        assertThrows(NoSuchElementException.class, () -> list.removeFirst(),
                "Throw an NoSuchElementException if user tries to remove an element from an empty list.");
    }

    @Test
    @DisplayName("Add three elements and remove from back.")
    public void testAddThreeRemoveFromBack() {
        list.addFirst("1");
        list.addFirst("2");
        list.addFirst("3");

        // remove first element from back
        assertEquals("1", list.removeLast(), "Third element in list incorrect.");

        // properties
        assertEquals(2, list.getSize(), "Size of list must be 2.");
        assertFalse(list.isEmpty(), "Method isEmpty() must return false for a list of size 2.");

        // iterator over remaining list
        Iterator<String> iterator = list.iterator();
        assertTrue(iterator.hasNext(), "Iterator must return true for hasNext() method.");
        assertEquals("3", iterator.next(), "First element in list incorrect.");
        assertEquals("2", iterator.next(), "Second element in list incorrect.");
        assertFalse(iterator.hasNext(), "Iterator must return false for hasNext() method.");

        // remove remaining elements from back
        assertEquals("2", list.removeLast(), "Second element in list incorrect.");
        assertEquals("3", list.removeLast(), "First element in list incorrect.");

        // check that list is now empty
        assertEquals(0, list.getSize(), "Size of list must be 0.");
        assertTrue(list.isEmpty(), "Method isEmpty() must return true for an empty list.");

        assertThrows(NoSuchElementException.class, () -> list.removeLast(),
                "Throw an NoSuchElementException if user tries to remove an element from an empty list.");
    }
}
