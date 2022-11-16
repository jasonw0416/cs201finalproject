package web_scraper;
import java.util.List;
public class classes_list {
		private List<classes> data = null;
		
		public classes_list(List<classes> stocks) {
			this.data = stocks;
		}
		
		public List<classes> getData() {
			return data;
		}
		
		public void setData(List<classes> data) {
			this.data = data;
		}
}
