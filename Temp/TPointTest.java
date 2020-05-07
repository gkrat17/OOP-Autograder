
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

public class TPointTest {

    private TPoint p1, p2;

    @BeforeEach
    protected void setUp() {
        p1 = new TPoint(0, 0);	
        p2 = new TPoint(p1);
    }

	@Test
	public void test1() {
        assertTrue(p1.equals(p1));
    }

	@Test
	public void test2() {
        assertFalse(p1.equals(""));
    }

	@Test
	public void test3() {
        assertTrue(p1.equals(p2));
    }

	@Test
	public void test4() {
        p2.x = 1;
        assertFalse(p1.equals(p2));
    }

	@Test
	public void test5() {
        p2.y = 1;
        assertFalse(p1.equals(p2));
    }

    @Test
    public void test6() {
        assertEquals(p1.toString(), "(0,0)");
    }
}
