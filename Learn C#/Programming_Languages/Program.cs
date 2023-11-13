using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace ProgrammingLanguages
{
	class Program
	{
		static void Main()
		{
			// Task 12
			// Skip the first line as it is a description of the data
			// Next modify each string; line, into a Language object
			// Convert the IEnumerable<Language> to a List<Language> using ToList()
			List<Language> languages = File.ReadAllLines("./languages.tsv")
			  .Skip(1) 
			  .Select(line => Language.FromTsv(line)) 
			  .ToList();

			Task1(languages);
			Task2(languages);
			Task3(languages);
			Task4(languages);
			Task5(languages);
			Task6(languages);
			Task7(languages);
			Task8(languages);
			Task9(languages);
		}
		private static void Task1(List<Language> languages)
		{
			Console.WriteLine("\nTask 1");
			PrettyPrintAll(languages);
		}


		private static void Task2(List<Language> languages)
		{
			Console.WriteLine("\nTask 2");
			var languagesFromLinq = languages.Select(lang => $"{lang.Year}, {lang.Name}, {lang.ChiefDeveloper}, {lang.Predecessors}");
			Console.WriteLine($"Number of languages: {languagesFromLinq.Count()}");
			PrintAll(languagesFromLinq);
		}


		private static void Task3(List<Language> languages)
		{
			Console.WriteLine("\nTask 3");
			var csharp = languages.Where(lang => lang.Name == "C#");
			Console.WriteLine($"Number of languages: {csharp.Count()}");
			PrettyPrintAll(csharp);
		}


		private static void Task4(List<Language> languages)
		{
			Console.WriteLine("\nTask 4");
			var microsoft = languages.Where(lang => lang.ChiefDeveloper.Contains("Microsoft"));
			PrettyPrintAll(microsoft);
		}


		private static void Task5(List<Language> languages)
		{
			Console.WriteLine("\nTask 5");
			var descendantsOfLisp = languages.Where(language => language.Predecessors.Contains("Lisp"));
			Console.WriteLine($"Number of languages: {descendantsOfLisp.Count()}");
			PrettyPrintAll(descendantsOfLisp);
		}


		private static void Task6(List<Language> languages)
		{
			Console.WriteLine("\nTask 6");
			var scriptLanguages = languages.Where(language => language.Name.Contains("Script"));
			Console.WriteLine($"Number of languages: {scriptLanguages.Count()}");
			PrettyPrintAll(scriptLanguages);
		}

		private static void Task7(List<Language> languages)
		{
			Console.WriteLine("\nTask 7");
			Console.WriteLine($"Total number of Languages: {languages.Count}");
		}

		private static IEnumerable<Language> Task8(List<Language> languages)
		{
			Console.WriteLine("\nTask 8");
			var between1995And2005 = from language in languages
									 where language.Year >= 1995 && language.Year <= 2005
									 select language;
			Console.WriteLine($"Languages between 1995 and 2005: {between1995And2005.Count()}");			
			return between1995And2005;
		}

		private static void Task9(List<Language> languages)
		{
			Console.WriteLine("\nTask 9");
			var between1995And2005 = Task8(languages);
			var modify = between1995And2005.Select(lang => $"{lang.Name} was inveted in {lang.Year}");
			PrintAll(modify);
		}

		// Task 10
		private static void PrettyPrintAll(IEnumerable<Language> enumLanguages)
		{
			foreach(Language language in enumLanguages)
			{
				Console.WriteLine(language.Prettify());
			}
		}

		// Task 11
		private static void PrintAll(IEnumerable<Object> objectLanguages)
		{
			foreach(Object objectLang in objectLanguages)
			{
				Console.WriteLine(objectLang);
			}

		}


	}


}
