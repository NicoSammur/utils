// Dumb Web Server for testing tools
// Execute and run http://ip:1234

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Net.Sockets;

namespace DumbWebServer
{
    class Program
    {
        static void Main(string[] args)
        {
            int port = 1234;
            TcpListener listener = new TcpListener(port); // Now is a deprecated method. Still works :B
            listener.Start();

            while (true)
            {
                Console.WriteLine("[+] Waiting for connections...");
                TcpClient client = listener.AcceptTcpClient();
                StreamReader sr = new StreamReader(client.GetStream());
                StreamWriter sw = new StreamWriter(client.GetStream());

                try
                {
                    // Client Request
                    string request = sr.ReadLine();
                    Console.WriteLine(request);
                    string[] t = request.Split(' ');
                    string page = t[1];

                    if (page == "/")
                    {
                        page = "/index.html";
                    }

                    // Find the file
                    StreamReader file = new StreamReader("../../htdocs" + page);
                    sw.WriteLine("HTTP/1.0 200 OK/n");

                    // Send the file
                    string data = file.ReadLine();
                    while (data != null)
                    {
                        sw.WriteLine(data);
                        sw.Flush();
                        data = file.ReadLine();
                    }

                }
                catch (Exception)
                {
                    sw.WriteLine("HTTP/1.0 404 OK\n"); // Not really
                    sw.WriteLine("<h1>404! - Hmmm I think that file don't exist!</h1>");
                    sw.Flush();
                }
                client.Close();
            }
        }
    }
}
