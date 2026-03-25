import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 5000); // server ke address aur port
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            
            // message bhejna
            out.println("Hello Server!");
            
            // server se reply lena
            String reply = in.readLine();
            System.out.println("Server ka reply: " + reply);
            
            socket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}