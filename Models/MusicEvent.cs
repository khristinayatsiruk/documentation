namespace MusicEventsApp.Models;

public class MusicEvent {
    public int Id { get; set; }
    public string Title { get; set; }
    public string Artist { get; set; }
    public string City { get; set; }
    public decimal Price { get; set; }
}