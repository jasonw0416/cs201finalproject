package web_scraper;

import java.io.FileWriter;
import java.io.IOException;
import java.net.MalformedURLException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.DomNode;
import com.gargoylesoftware.htmlunit.html.DomNodeList;
import com.gargoylesoftware.htmlunit.html.HtmlElement;
import com.gargoylesoftware.htmlunit.html.HtmlPage;
import com.gargoylesoftware.htmlunit.html.HtmlTable;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;



public class HTML_unit {
	
	public static void main(String[] args) {
		WebClient webClient = new WebClient();
		webClient.getOptions().setCssEnabled(false);
		webClient.getOptions().setJavaScriptEnabled(false);
		List<classes> list=new ArrayList<classes>();
		// GE A
		HtmlPage page = null;
			try {
				page = webClient.getPage("https://classes.usc.edu/term-20223/classes/arts/");
			}
			catch (Exception e) {
				System.out.println("Fuck");
			}
		String selector = ".course-info";
		DomNodeList<DomNode> rows = page.querySelectorAll(selector);
		System.out.println(rows.size());
		for (DomNode row: rows) {
			String courseName = row.getFirstChild().getFirstChild().querySelector(".courselink").asNormalizedText();
			DomNode course_details = row.getLastChild().getLastChild();
			System.out.println(course_details);
			DomNode table_body = course_details.getFirstChild();
			DomNodeList<DomNode> table_rows = table_body.getChildNodes();
			System.out.println(table_rows.size());
			int i = 1;
			for(DomNode child: table_rows) {
				if (i != 1) {
					String section = "";
					String time = "";
					String days = "";
					String instructor = "";
					if (child.querySelector(".section") != null) {
						section = child.querySelector(".section").asNormalizedText();
					}
					if (child.querySelector(".time") != null) {
						time = child.querySelector(".time").asNormalizedText();
					}
					if (child.querySelector(".days") != null) {
						days = child.querySelector(".days").asNormalizedText();
					}
					if (child.querySelector(".instructor") != null) {
						instructor = child.querySelector(".instructor").asNormalizedText();
					}
					String GE_category = "A";
					if (section != null && time != null && days != null && instructor != null && courseName != null) {
						list.add(new classes(section, courseName, instructor, days, time, GE_category));
					}
				}
				i += 1;
			}
			
		}
		// GE B
		page = null;
		try {
			page = webClient.getPage("https://classes.usc.edu/term-20223/classes/hinq/");
		}
		catch (Exception e) {
			System.out.println("Fuck");
		}
		selector = ".course-info";
		rows = page.querySelectorAll(selector);
		System.out.println(rows.size());
		for (DomNode row: rows) {
			String courseName = row.getFirstChild().getFirstChild().querySelector(".courselink").asNormalizedText();
			DomNode course_details = row.getLastChild().getLastChild();
			System.out.println(course_details);
			DomNode table_body = course_details.getFirstChild();
			DomNodeList<DomNode> table_rows = table_body.getChildNodes();
			System.out.println(table_rows.size());
			int i = 1;
			for(DomNode child: table_rows) {
				if (i != 1) {
					String section = "";
					String time = "";
					String days = "";
					String instructor = "";
					if (child.querySelector(".section") != null) {
						section = child.querySelector(".section").asNormalizedText();
					}
					if (child.querySelector(".time") != null) {
						time = child.querySelector(".time").asNormalizedText();
					}
					if (child.querySelector(".days") != null) {
						days = child.querySelector(".days").asNormalizedText();
					}
					if (child.querySelector(".instructor") != null) {
						instructor = child.querySelector(".instructor").asNormalizedText();
					}
					System.out.println(section + time + days + instructor);
					String GE_category = "B";
					if (section != "" && time != "" && days != "" && instructor != "" && courseName != "") {
						list.add(new classes(section, courseName, instructor, days, time, GE_category));
					}
				}
				i += 1;
			}
			
		}
		// GE C
		page = null;
		try {
			page = webClient.getPage("https://classes.usc.edu/term-20223/classes/sana/");
		}
		catch (Exception e) {
			System.out.println("Fuck");
		}
		selector = ".course-info";
		rows = page.querySelectorAll(selector);
		System.out.println(rows.size());
		for (DomNode row: rows) {
			String courseName = row.getFirstChild().getFirstChild().querySelector(".courselink").asNormalizedText();
			DomNode course_details = row.getLastChild().getLastChild();
			System.out.println(course_details);
			DomNode table_body = course_details.getFirstChild();
			DomNodeList<DomNode> table_rows = table_body.getChildNodes();
			System.out.println(table_rows.size());
			int i = 1;
			for(DomNode child: table_rows) {
				if (i != 1) {
					String section = "";
					String time = "";
					String days = "";
					String instructor = "";
					if (child.querySelector(".section") != null) {
						section = child.querySelector(".section").asNormalizedText();
					}
					if (child.querySelector(".time") != null) {
						time = child.querySelector(".time").asNormalizedText();
					}
					if (child.querySelector(".days") != null) {
						days = child.querySelector(".days").asNormalizedText();
					}
					if (child.querySelector(".instructor") != null) {
						instructor = child.querySelector(".instructor").asNormalizedText();
					}
					System.out.println(section + time + days + instructor);
					String GE_category = "C";
					if (section != null && time != null && days != null && instructor != null && courseName != null) {
						list.add(new classes(section, courseName, instructor, days, time, GE_category));
					}
				}
				i += 1;
			}
			
		}
		
		// GE D
		page = null;
		try {
			page = webClient.getPage("https://classes.usc.edu/term-20223/classes/life/");
		}
		catch (Exception e) {
			System.out.println("Fuck");
		}
		selector = ".course-info";
		rows = page.querySelectorAll(selector);
		System.out.println(rows.size());
		for (DomNode row: rows) {
			String courseName = row.getFirstChild().getFirstChild().querySelector(".courselink").asNormalizedText();
			DomNode course_details = row.getLastChild().getLastChild();
			System.out.println(course_details);
			DomNode table_body = course_details.getFirstChild();
			DomNodeList<DomNode> table_rows = table_body.getChildNodes();
			System.out.println(table_rows.size());
			int i = 1;
			for(DomNode child: table_rows) {
				if (i != 1) {
					String section = "";
					String time = "";
					String days = "";
					String instructor = "";
					if (child.querySelector(".section") != null) {
						section = child.querySelector(".section").asNormalizedText();
					}
					if (child.querySelector(".time") != null) {
						time = child.querySelector(".time").asNormalizedText();
					}
					if (child.querySelector(".days") != null) {
						days = child.querySelector(".days").asNormalizedText();
					}
					if (child.querySelector(".instructor") != null) {
						instructor = child.querySelector(".instructor").asNormalizedText();
					}
					System.out.println(section + time + days + instructor);
					String GE_category = "D";
					if (section != null && time != null && days != null && instructor != null && courseName != null) {
						list.add(new classes(section, courseName, instructor, days, time, GE_category));
					}
				}
				i += 1;
			}
			
		}
		
		// GE E
		page = null;
		try {
			page = webClient.getPage("https://classes.usc.edu/term-20223/classes/psc/");
		}
		catch (Exception e) {
			System.out.println("Fuck");
		}
		selector = ".course-info";
		rows = page.querySelectorAll(selector);
		System.out.println(rows.size());
		for (DomNode row: rows) {
			String courseName = row.getFirstChild().getFirstChild().querySelector(".courselink").asNormalizedText();
			DomNode course_details = row.getLastChild().getLastChild();
			System.out.println(course_details);
			DomNode table_body = course_details.getFirstChild();
			DomNodeList<DomNode> table_rows = table_body.getChildNodes();
			System.out.println(table_rows.size());
			int i = 1;
			for(DomNode child: table_rows) {
				if ( i != 1) {
					String section = "";
					String time = "";
					String days = "";
					String instructor = "";
					if (child.querySelector(".section") != null) {
						section = child.querySelector(".section").asNormalizedText();
					}
					if (child.querySelector(".time") != null) {
						time = child.querySelector(".time").asNormalizedText();
					}
					if (child.querySelector(".days") != null) {
						days = child.querySelector(".days").asNormalizedText();
					}
					if (child.querySelector(".instructor") != null) {
						instructor = child.querySelector(".instructor").asNormalizedText();
					}
					System.out.println(section + time + days + instructor);
					String GE_category = "E";
					if (section != null && time != null && days != null && instructor != null && courseName != null) {
						list.add(new classes(section, courseName, instructor, days, time, GE_category));
					}
				}
				i += 1;
			}
			
		}
		
		// GE F
		page = null;
		try {
			page = webClient.getPage("https://classes.usc.edu/term-20223/classes/qrea/");
		}
		catch (Exception e) {
			System.out.println("Fuck");
		}
		selector = ".course-info";
		rows = page.querySelectorAll(selector);
		System.out.println(rows.size());
		for (DomNode row: rows) {
			String courseName = row.getFirstChild().getFirstChild().querySelector(".courselink").asNormalizedText();
			DomNode course_details = row.getLastChild().getLastChild();
			System.out.println(course_details);
			DomNode table_body = course_details.getFirstChild();
			DomNodeList<DomNode> table_rows = table_body.getChildNodes();
			System.out.println(table_rows.size());
			int i = 1;
			for(DomNode child: table_rows) {
				if (i != 1) {
					String section = "";
					String time = "";
					String days = "";
					String instructor = "";
					if (child.querySelector(".section") != null) {
						section = child.querySelector(".section").asNormalizedText();
					}
					if (child.querySelector(".time") != null) {
						time = child.querySelector(".time").asNormalizedText();
					}
					if (child.querySelector(".days") != null) {
						days = child.querySelector(".days").asNormalizedText();
					}
					if (child.querySelector(".instructor") != null) {
						instructor = child.querySelector(".instructor").asNormalizedText();
					}
					System.out.println(section + time + days + instructor);
					String GE_category = "F";
					if (section != null && time != null && days != null && instructor != null && courseName != null) {
						list.add(new classes(section, courseName, instructor, days, time, GE_category));
					}
				}
				i += 1;
			}
			
		}
		
		// GE G
		page = null;
		try {
			page = webClient.getPage("https://classes.usc.edu/term-20223/classes/gpg/");
		}
		catch (Exception e) {
			System.out.println("Fuck");
		}
		selector = ".course-info";
		rows = page.querySelectorAll(selector);
		System.out.println(rows.size());
		for (DomNode row: rows) {
			String courseName = row.getFirstChild().getFirstChild().querySelector(".courselink").asNormalizedText();
			DomNode course_details = row.getLastChild().getLastChild();
			System.out.println(course_details);
			DomNode table_body = course_details.getFirstChild();
			DomNodeList<DomNode> table_rows = table_body.getChildNodes();
			System.out.println(table_rows.size());
			int i = 1;
			for(DomNode child: table_rows) {
				if (i != 1) {
					String section = "";
					String time = "";
					String days = "";
					String instructor = "";
					if (child.querySelector(".section") != null) {
						section = child.querySelector(".section").asNormalizedText();
					}
					if (child.querySelector(".time") != null) {
						time = child.querySelector(".time").asNormalizedText();
					}
					if (child.querySelector(".days") != null) {
						days = child.querySelector(".days").asNormalizedText();
					}
					if (child.querySelector(".instructor") != null) {
						instructor = child.querySelector(".instructor").asNormalizedText();
					}
					System.out.println(section + time + days + instructor);
					String GE_category = "G";
					if (section != null && time != null && days != null && instructor != null && courseName != null) {
						list.add(new classes(section, courseName, instructor, days, time, GE_category));
					}
				}
				i += 1;
			}
			
		}
		// GE H
		page = null;
		try {
			page = webClient.getPage("https://classes.usc.edu/term-20223/classes/gph/");
		}
		catch (Exception e) {
			System.out.println("Fuck");
		}
		selector = ".course-info";
		rows = page.querySelectorAll(selector);
		System.out.println(rows.size());
		for (DomNode row: rows) {
			String courseName = row.getFirstChild().getFirstChild().querySelector(".courselink").asNormalizedText();
			DomNode course_details = row.getLastChild().getLastChild();
			System.out.println(course_details);
			DomNode table_body = course_details.getFirstChild();
			DomNodeList<DomNode> table_rows = table_body.getChildNodes();
			System.out.println(table_rows.size());
			int i = 1;
			for(DomNode child: table_rows) {
				if (i != 1) {
					String section = "";
					String time = "";
					String days = "";
					String instructor = "";
					if (child.querySelector(".section") != null) {
						section = child.querySelector(".section").asNormalizedText();
					}
					if (child.querySelector(".time") != null) {
						time = child.querySelector(".time").asNormalizedText();
					}
					if (child.querySelector(".days") != null) {
						days = child.querySelector(".days").asNormalizedText();
					}
					if (child.querySelector(".instructor") != null) {
						instructor = child.querySelector(".instructor").asNormalizedText();
					}
					System.out.println(section + time + days + instructor);
					String GE_category = "H";
					if (section != null && time != null && days != null && instructor != null && courseName != null) {
						list.add(new classes(section, courseName, instructor, days, time, GE_category));
					}
				}
				i += 1;
			}
			
		}
		classes_list InsertedJsonData = new classes_list(list);
		Gson gson = new GsonBuilder()
		        .setPrettyPrinting().disableHtmlEscaping()
		        .create();
		String json = gson.toJson(InsertedJsonData);
		try {
			FileWriter writer = new FileWriter("stock.json");
			writer.write(json);
			writer.close();
		}
		catch(IOException e) {
			e.printStackTrace();
		}
		
	}
}
