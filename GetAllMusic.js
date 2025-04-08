let musiques = [];  // Liste des musiques récupérées (sans doublons)
let lastHeight = 0; // Hauteur de la page pour vérifier les changements

// Fonction pour récupérer les musiques
function getMusiques() {
  const h6Elements = document.querySelectorAll('h6');
  const h6Texts = Array.from(h6Elements).map(h6 => h6.textContent.trim());

  for (let i = 0; i < h6Texts.length; i++) {
    // Si l'élément n'est pas un numéro, c'est un titre ou un artiste
    if (isNaN(h6Texts[i])) {
      const titre = h6Texts[i];
      const artiste = h6Texts[i + 1] || 'Artiste inconnu';

      // Vérifier si la musique existe déjà (éviter les doublons)
      const musiqueExistante = musiques.some(m => m.titre === titre && m.artiste === artiste);
      if (!musiqueExistante) {
        musiques.push({ titre, artiste });
      }
      i++; // Passer à l'artiste suivant
    }
  }
  console.log(`Musiques récupérées : ${musiques.length}`);
}

// Fonction pour observer le défilement de la page
function observeScroll() {
  // On écoute le scroll et on vérifie si la page a atteint le bas
  window.addEventListener('scroll', function() {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
      // Si la page est arrivée en bas, récupérer les nouvelles musiques
      getMusiques();
    }
  });
}

// Fonction pour vérifier si de nouveaux éléments sont ajoutés au DOM
function checkForNewElements() {
  const currentHeight = document.body.scrollHeight;

  // Si la hauteur de la page a changé, récupérer les nouvelles musiques
  if (currentHeight > lastHeight) {
    getMusiques();
    lastHeight = currentHeight;
  }
}

// Lancer l'observation dès que la page est prête
observeScroll();

// Vérifier périodiquement si de nouveaux éléments ont été ajoutés
setInterval(checkForNewElements, 1000); // Toutes les 1 seconde

// Fonction pour exporter les musiques dans un fichier JSON
function exportMusiques() {
  // Créer un fichier Blob avec les données des musiques
  const blob = new Blob([JSON.stringify(musiques, null, 2)], { type: 'application/json' });
  
  // Créer une URL pour le Blob
  const url = URL.createObjectURL(blob);
  
  // Créer un élément <a> pour télécharger le fichier
  const a = document.createElement('a');
  a.href = url;
  a.download = 'musiques.json'; // Nom du fichier à télécharger
  document.body.appendChild(a);
  a.click(); // Simuler un clic sur le lien pour télécharger le fichier
  
  // Nettoyer en supprimant l'élément <a> et révoquer l'URL
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  
  console.log("Export des musiques réussi !");
}

// Utiliser exportMusiques() dans un 2e temps après avoir scrollé
