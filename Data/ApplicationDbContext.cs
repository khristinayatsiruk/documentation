using Microsoft.EntityFrameworkCore;
using MusicEventsApp.Models;

namespace MusicEventsApp.Data;

public class ApplicationDbContext : DbContext {
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }
    public DbSet<MusicEvent> MusicEvents { get; set; }
}